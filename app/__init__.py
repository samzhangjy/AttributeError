# app/__init__.py

import os

from flask import Flask  # 导入Flask
from .extensions import *  # 导入已经实例化了的扩展
from app.config import config  # 导入config
from .models import User


def create_app():
    app = Flask(__name__)  # 创建app实例
    # 设置从config中导入设置，如果没有设置环境，则从default导入
    app.config.from_object(config[os.environ.get('FLASK_ENV') or 'default'])

    # 初始化扩展
    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    avatars.init_app(app)

    @login_manager.user_loader  # 定义用户加载器
    def load_user(id):
        return User.query.get(id)

    from .main import main as main_bp  # 导入蓝图
    app.register_blueprint(main_bp)  # 注册蓝图到应用

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    from .user import user as user_bp
    app.register_blueprint(user_bp)

    return app  # 返回app
