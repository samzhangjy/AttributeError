# app/models.py
from flask import current_app
from itsdangerous import Serializer

from .extensions import db, bcrypt
from flask_login import UserMixin
from datetime import datetime
from flask_avatars import Identicon


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    users = db.relationship('User', backref='role', lazy='dynamic')  # 创建一个关联

    @staticmethod
    def insert_role():
        print('Inserting roles...', end='')
        roles = ['普通用户', '协管员', '管理员']
        for role in roles:
            if Role.query.filter_by(name=role).first() is None:
                role = Role(name=role)
                db.session.add(role)
        db.session.commit()
        for user in User.query.all():
            if user.role is None:
                user.role = Role.query.filter_by(name='普通用户').first()
                db.session.add(user)
        db.session.commit()
        print('done')

    def __repr__(self):
        return '<Role %s>' % self.name


class User(db.Model, UserMixin):  # User类继承自db.Model
    __tablename__ = 'users'  # 定义表名
    id = db.Column(db.Integer, primary_key=True)  # 定义id，并且为主键
    username = db.Column(db.String(64))  # 用户名
    email = db.Column(db.String(128))  # 邮箱地址
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    password = db.Column(db.String(255))  # 存放密码
    confirmed = db.Column(db.Boolean, default=False)
    real_name = db.Column(db.String(64))  # 真实名称
    about = db.Column(db.Text)  # 自我简介
    member_since = db.Column(db.DateTime, default=datetime.utcnow())  # 注册时间
    gender = db.Column(db.String(64))
    site = db.Column(db.String(256))
    avatar_s = db.Column(db.String(128))
    avatar_m = db.Column(db.String(128))
    avatar_l = db.Column(db.String(128))
    raw_avatar = db.Column(db.String(128))
    background = db.Column(db.String(128))

    def __init__(self, password, **kwargs):
        super().__init__(password=password, **kwargs)
        self.password = self.set_password(password)  # 初始化时将未加密的密码加密
        self.generate_avatar()

    def generate_avatar(self):
        avatar = Identicon()
        filenames = avatar.generate(text=self.username)
        self.avatar_s = filenames[0]
        self.avatar_m = filenames[1]
        self.avatar_l = filenames[2]
        db.session.commit()

    def set_password(self, password):
        return bcrypt.generate_password_hash(password)  # 调用Flask-Bcrypt内置函数生成密码哈希值

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)  # 检查密码是否与哈希值对应

    def generate_confirmation_token(self):
        s = Serializer(secret_key=current_app.config['SECRET_KEY'])
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def __repr__(self):  # 定义User类的返回名称
        return '<User %s>' % self.username  # 返回 <User 用户名>
