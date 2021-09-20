
from httpRequest import HttpRequest


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
    def search_by_keyword(cls, keyword):
        url = YushuBook.keyword_url.format(keyword, count, start)
        # dict
        result = HttpRequest.get(url)
        return result

