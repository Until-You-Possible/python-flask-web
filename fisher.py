
# @Time    : 9/20/2021 10:47 AM
# @Author  : arthur
# @Email   : arthurwanggang@outlook.com
# @File    : fisher.py
# @Software: PyCharm

from app import create_app

app = create_app()

if __name__ == '__main__':
    # 生产环境 nginx+uwsgi
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
