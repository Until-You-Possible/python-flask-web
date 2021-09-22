# @Time    : 9/22/2021 10:47 AM
# @Author  : arthur
# @Email   : arthurwanggang@outlook.com
# @File    : yushu_book.py
# @Software: PyCharm


from httpRequest import HttpRequest
from flask import current_app


class YushuBook:
    isbn_url = "http://t.talelin.com/v2/book/isbn/{}"
    keyword_url = "http://t.talelin.com/v2/book/search/?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = YushuBook.isbn_url.format(isbn)
        # dict
        result = HttpRequest.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = YushuBook.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        # dict
        result = HttpRequest.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
