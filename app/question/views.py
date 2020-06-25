# app/question/views.py
from . import question
from flask_login import current_user, login_required
from flask import request, render_template, flash, redirect, url_for
from ..models import Question
from ..extensions import db
from .forms import AddQuestionForm


@question.route('/add/', methods=['GET', 'POST'])
@login_required
def add():
    form = AddQuestionForm()
    if form.validate_on_submit():
        title = form.title.data
        body_markdown = form.body_markdown.data
        # 获取Editor.md自动生成的HTML
        body_html = request.form['editormd-html-code']
        # 创建问题
        _question = Question(
            title=title, body_markdown=body_markdown, body_html=body_html, author=current_user)
        db.session.add(_question)
        # 保存到数据库
        db.session.commit()
        flash('添加问题成功！', category='success')
        return redirect(url_for('main.index'))
    return render_template('question/add.html', form=form)
