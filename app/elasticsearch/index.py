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
source_path = "/Users/wanggang/Documents/kba/kba.json"
index_name = "kba"
index_type = "_doc"
with open(source_path, 'r', encoding='utf8') as fp:
    json_data = json.load(fp, strict=False)
    for item in json_data:
        count += 1
        action = {
            "_index": index_name,
            "_type": index_type,
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

