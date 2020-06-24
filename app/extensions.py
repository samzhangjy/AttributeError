# app/extensions.py

from flask_bootstrap import Bootstrap  # 导入Bootstrap-Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_avatars import Avatars

# 实例化扩展
bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "auth.login"  # 定义flask-login的登录视图
login_manager.login_message = "请登录后再访问本页"  # 定义flask-login的登录消息，默认为'Please log in to access this page.'
mail = Mail()
moment = Moment()
avatars = Avatars()
