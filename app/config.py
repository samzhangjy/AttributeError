# app/config.py

import os


class DevelopmentConfig:
    DEBUG = True  # 设置为调试模式
    # 设置数据库位置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or 'mysql+pymysql://root:%s@localhost:3306/%s' \
                                                                    '?charset'\
                                                                    '=utf8mb4' % (os.environ.get('DEV_DATABASE_PASS'),
                                                                                  os.environ.get('DEV_DATABASE_NAME'))
    # 不跟踪变化
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig:
    DEBUG = False  # 关闭调试
    # 设置在生产环境中使用的数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'mysql+pymysql://root:%s@localhost:3306/%s?charset' \
                               '=utf8mb4' % (os.environ.get('DATABASE_PASS'), os.environ.get('DATABASE_NAME'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 设置在不同情况下使用的config
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
