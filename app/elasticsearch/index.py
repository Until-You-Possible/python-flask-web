from elasticsearch import Elasticsearch
import json
import time
from elasticsearch import helpers
from elasticsearch import Elasticsearch

es = Elasticsearch('http://127.0.0.1:9200')
print(es.info())
count = 0
start_time = time.time()
actions = []
with open('/Users/wanggang/Documents/kba/kba.json', 'r', encoding='utf8') as fp:
    json_data = json.load(fp, strict=False)
    for item in json_data:
        count += 1
        action = {
            "_index": "test",
            "_type": "_doc",
            "source": item
        }
        actions.append(action)
        if len(actions) == 1000:
            helpers.bulk(es, actions)
            actions = []
    helpers.bulk(es, actions)
    print("总共有数据", count)
    end_time = time.time()
    t = end_time - start_time
    print("已经被导入数据", count, "耗时", t)

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         print('共耗时约 {:.2f} 秒'.format(time.time() - start))
#         return res
#
#     return wrapper
#
#
# @timer
# def create_data():
#     """ 写入数据 """
#     for line in range(100):
#         es.index(index='s2', doc_type='doc', body={'title': line})
