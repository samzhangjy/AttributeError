# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Regexp, Email, Length, EqualTo, ValidationError

from app.models import User


class RegistrationForm(FlaskForm):  # RegistrationForm继承自FlaskForm
    # StringField用来获取字符型数据，validators是验证器，Regexp中填写的是正则表达式
    username = StringField('用户名', validators=[DataRequired(message='请输入用户名'), Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
                                                                                     0, '用户名只能包含字母，数字，点'
                                                                                        '或下划线'), Length(1, 64)])
    # Email验证器用来验证输入是否是邮箱格式，但不确保邮箱是否存在
    email = StringField('邮箱', validators=[DataRequired(message='请输入邮箱'), Email(message='请输入真实的邮箱地址')])
    password = PasswordField('密码', validators=[DataRequired(message='请输入密码'), EqualTo('password2', message='密码不一致')])
    password2 = PasswordField('确认密码', validators=[DataRequired(message='请输入确认密码')])
    submit = SubmitField('注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已被注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册')


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(message='请输入用户名')])
    password = PasswordField('密码', validators=[DataRequired(message='请输入密码')])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')
