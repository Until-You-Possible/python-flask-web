from elasticsearch import Elasticsearch

import time
from elasticsearch import Elasticsearch

es = Elasticsearch('192.168.1.1:9200')


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print('共耗时约 {:.2f} 秒'.format(time.time() - start))
        return res

    return wrapper


@timer
def create_data():
    """ 写入数据 """
    for line in range(100):
        es.index(index='s2', doc_type='doc', body={'title': line})
