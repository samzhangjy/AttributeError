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
    SECRET_KEY = 'this is my secret key!!'  # 设置密钥
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    AVATARS_SAVE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/avatars/')
    BACKGROUNDS_SAVE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/bg/')


class ProductionConfig:
    DEBUG = False  # 关闭调试
    # 设置在生产环境中使用的数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'mysql+pymysql://root:%s@localhost:3306/%s?charset' \
                               '=utf8mb4' % (os.environ.get('DATABASE_PASS'), os.environ.get('DATABASE_NAME'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret key'  # 生产环境首先使用环境变量中的密钥
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    AVATARS_SAVE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/avatars/')
    BACKGROUNDS_SAVE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/bg/')


# 设置在不同情况下使用的config
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
