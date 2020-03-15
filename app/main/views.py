from flask import render_template  # 导入渲染模板函数
from . import main  # 导入蓝图


@main.route('/')  # 定义路由
def index():
    return render_template('main/index.html')  # 返回渲染后的页面正文
