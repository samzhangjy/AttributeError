# app/question/__init__.py

from flask import Blueprint

question = Blueprint('question', __name__, url_prefix='/question')

from . import views
