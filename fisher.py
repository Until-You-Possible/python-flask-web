from app import create_app

app = create_app()

if __name__ == '__main__':
    # 生产环境 nginx+uwsgi
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
