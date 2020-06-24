# app/user/__init__.py

from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='/user')

from . import views
