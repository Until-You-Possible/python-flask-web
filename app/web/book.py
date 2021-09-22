# @Time    : 9/22/2021 10:47 AM
# @Author  : arthur
# @Email   : arthurwanggang@outlook.com
# @File    : book.py
# @Software: PyCharm


from flask import jsonify, Blueprint, request

import app.forms.book
from helper import is_isbn_or_key
from yushu_book import YushuBook
from . import web
from app.forms.book import SearchForm


@web.route("/book/search")
def search():
    """
       q: 关键字keyword 或者 isbn
       page
    """
    # 对参数的各种判断
    # q = request.args['q']
    # page = request.args['page']
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YushuBook.search_by_isbn(q)
        else:
            result = YushuBook.search_by_keyword(q, page)
        return jsonify(result)
        # return result
    else:
        return jsonify(form.errors)
