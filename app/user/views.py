# app/user/views.py
import os

from flask_login import current_user, login_required

from . import user
from flask import render_template, abort, request, url_for, send_from_directory, redirect, flash, current_app

from ..extensions import avatars, db
from ..models import User


@user.route('/<username>/')
def user_profile(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user/user-profile.html', user=user)


@user.route('/avatars/<path:filename>')
def get_avatar(filename):
    return send_from_directory('static/avatars', filename)


@user.route('/change-avatar/', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        raw_filename = avatars.save_avatar(f)
        u = current_user._get_current_object()
        u.raw_avatar = raw_filename
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('user.crop'))
    return render_template('user/change-avatar-upload.html')


@user.route('/change-avatar/crop/', methods=['GET', 'POST'])
@login_required
def crop():
    if request.method == 'POST':
        x = request.form.get('x')
        y = request.form.get('y')
        w = request.form.get('w')
        h = request.form.get('h')
        filenames = avatars.crop_avatar(current_user.raw_avatar, x, y, w, h)
        u = current_user._get_current_object()
        u.avatar_s = filenames[0]
        u.avatar_m = filenames[1]
        u.avatar_l = filenames[2]
        db.session.add(u)
        db.session.commit()
        flash('更改头像成功', 'success')
        return redirect(url_for('user.user_profile', username=u.username))
    return render_template('user/change-avatar-crop.html')


@user.route('/change-avatar/default/')
@login_required
def default_avatar():
    u = current_user._get_current_object()
    u.avatar_l = '%s_l.png' % u.username
    u.avatar_m = '%s_m.png' % u.username
    u.avatar_s = '%s_s.png' % u.username
    db.session.add(u)
    db.session.commit()
    flash('头像已恢复为默认头像', 'success')
    return redirect(url_for('user.user_profile', username=u.username))


@user.route('/change-bg/', methods=['GET', 'POST'])
def upload_background():
    if request.method == 'POST' and 'file' in request.files:
        file = request.files['file']
        ext = file.filename.rsplit('.', 1)[1].lower()
        filename = '%s_bg.%s' % (current_user.username, ext)
        file.save(os.path.join(current_app.config['BACKGROUNDS_SAVE_PATH'], filename))
        return redirect(url_for('uploaded_file', filename=filename))
