from flask import Flask

from app.web.book import web


def create_app():
    app = Flask(__name__)
    # 引入配置文件
    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    app.register_blueprint(web)
