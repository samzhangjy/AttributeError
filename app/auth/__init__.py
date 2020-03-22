# app/auth/__init__.py

from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')  # 设置URL前缀

from . import views
