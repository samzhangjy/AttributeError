# app/main/views.py

from flask import render_template, request  # 导入渲染模板函数
from . import main  # 导入蓝图
from flask_login import current_user


@main.route('/')  # 定义路由
def index():
    return render_template('main/index.html')  # 返回渲染后的页面正文
