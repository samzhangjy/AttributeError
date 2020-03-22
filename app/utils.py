# app/utils.py
from urllib.parse import urlparse, urljoin

from flask_mail import Message
from flask import render_template, current_app, request
from .extensions import mail
import threading


def send_async_email(msg):
    with current_app.app_context():
        mail.send(msg)


def send_email(from_address, to_address, title, template=None, **kwargs):
    msg = Message(title, sender=from_address, recipients=[to_address])  # 创建消息
    if template:
        msg.body = render_template('%s.txt' % template, **kwargs)  # 渲染文本正文
        msg.html = render_template('%s.html' % template, **kwargs)  # 渲染HTML正文
    else:
        msg.body = title
    threading.Thread(target=send_async_email, args=[msg])  # 异步发送邮件


def is_safe_url(target):
    ref_url = urlparse(request.host_url)  # 获取程序内的主机url
    test_url = urlparse(urljoin(request.host_url, target))  # 将目标URl转换为绝对路径
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc  # 验证是否属于内部url
