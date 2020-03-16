# app/extensions.py

from flask_bootstrap import Bootstrap  # 导入Bootstrap-Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 实例化扩展
bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
