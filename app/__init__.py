# @Time    : 9/22/2021 10:47 AM
# @Author  : arthur
# @Email   : arthurwanggang@outlook.com
# @File    : __init__.py
# @Software: PyCharm

from flask import Flask
from app.web.book import web
from app.models.book import db


def create_app():
    app = Flask(__name__)
    # 引入配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    app.register_blueprint(web)
