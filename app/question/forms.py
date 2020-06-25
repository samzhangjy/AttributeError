# app/question/forms.py

from wtforms import StringField, TextAreaField, HiddenField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class AddQuestionForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired()], render_kw={'autocomplete': 'off', 'autofocus': 'true'})
    body_markdown = TextAreaField('介绍')
    submit = SubmitField('添加问题')
