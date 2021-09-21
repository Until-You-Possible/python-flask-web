from flask import jsonify, Blueprint

from helper import is_isbn_or_key
from yushu_book import YushuBook

web = Blueprint('web', __name__)


@web.route("/book/search/<q>/<page>")
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
    return jsonify(result)
    # return result
