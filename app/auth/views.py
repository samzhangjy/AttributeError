# app/auth/views.py

from . import auth
from app.models import User, Role
from flask import render_template, flash, redirect, url_for, request
from .forms import RegistrationForm, LoginForm  # 导入表单
from app.extensions import db
from flask_login import login_user, login_required, logout_user, current_user
from app.utils import send_email, is_safe_url


@auth.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()  # 实例化表单
    if form.validate_on_submit():  # 当form被提交时执行
        # 获取表单信息
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user = User(username=username, email=email, password=password, role=Role.query.filter_by(name='普通用户').first())
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email('noreply@attributeerror.com', user.email, '认证你的账号', template='auth/email/confirm', user=user,
                   token=token)
        flash('注册成功，你现在可以登录了', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember_me.data
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user, remember=remember)
            next = request.args.get('next')
            flash('登录成功！', 'success')
            if next:  # 验证有没有next
                if is_safe_url(next):
                    return redirect(next)
            return redirect(url_for('main.index'))
        flash('用户名或密码不正确', 'warning')
    return render_template('auth/login.html', form=form)


@auth.route('/logout/')
@login_required  # 只有用户登录了才能登出
def logout():
    logout_user()
    flash('你已登出', 'success')
    return redirect(url_for('main.index'))


@auth.route('/confirm/<token>/')
@login_required
def confirm_user(token):
    user = current_user._get_current_object()
    if user.confirm(token):
        db.session.commit()
        flash('验证用户成功！', 'success')
        return redirect(url_for('main.index'))
    flash('令牌不正确，验证失败', 'error')
    return redirect(url_for('main.index'))


@auth.route('/confirm/re-send/')
@login_required
def re_send_confirm():
    user = current_user._get_current_object()
    token = user.generate_confirmation_token()
    send_email('noreply@attributeerror.com', user.email, '认证你的账号', template='auth/email/confirm', user=user,
               token=token)
    flash('一封新的验证邮件发送成功！', 'success')
    return redirect(url_for('main.index'))


@auth.route('/unconfirmed/')
@login_required
def unconfirmed():
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.before_app_request  # 在应用执行每一个请求之前执行的函数
def before_request():
    if not current_user.is_anonymous and not current_user.confirmed and request.blueprint != 'auth':
        return redirect(url_for('auth.unconfirmed'))
