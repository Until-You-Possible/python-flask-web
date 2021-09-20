from flask import Flask, make_response
from helper import is_isbn_or_key
from yushu_book import YushuBook

app = Flask(__name__)
# 引入配置文件
app.config.from_object('config')


@app.route("/book/search/<q>/<page>")
def search(q, page):
    """
       q: 关键字keyword 或者 isbn
       page
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YushuBook.search_by_isbn(q)
    else:
        result = YushuBook.search_by_keyword(q)
    return result


if __name__ == '__main__':
    # 生产环境 nginx+uwsgi
    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
