# app/models.py

from .extensions import db  # 导入SQLAlchemy


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    users = db.relationship('User', backref='role', lazy='dynamic')  # 创建一个关联

    def __repr__(self):
        return '<Role %s>' % self.name


class User(db.Model):  # User类继承自db.Model
    __tablename__ = 'users'  # 定义表名
    id = db.Column(db.Integer, primary_key=True)  # 定义id，并且为主键
    username = db.Column(db.String(64))  # 用户名
    email = db.Column(db.String(128))  # 邮箱地址
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def __repr__(self):  # 定义User类的返回名称
        return '<User %s>' % self.username  # 返回 <User 用户名>
