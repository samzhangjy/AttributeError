from flask import Blueprint  # 导入Flask中的蓝图

main = Blueprint('main', __name__)  # 创建一个名叫main的蓝图

from . import views  # 导入视图
