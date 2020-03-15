from flask import Flask  # 导入Flask
from .extensions import *  # 导入已经实例化了的扩展


def create_app():
    app = Flask(__name__)  # 创建app实例

    bootstrap.init_app(app)  # 初始化扩展

    from .main import main as main_bp  # 导入蓝图
    app.register_blueprint(main_bp)  # 注册蓝图到应用

    return app  # 返回app
