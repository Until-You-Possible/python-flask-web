import json

import jsonlines
from elasticsearch import Elasticsearch

url = "https://elasticsearch.ingress.forme-dev.forme.shoot.canary.k8s-hana.ondemand.com"
username = "admin"
password = "SAPForMeAdmin88&"

es = Elasticsearch('192.168.1.1:9200')
# 链接es成功
print(es.info())

mapping = {
    'properties': {
        'title': {
            'type': 'text',
            'analyzer': 'standard'
        }
    }
}

# es.indices.create(index='news', ignore=400)
# es.indices.put_mapping(index='news', doc_type='politics', include_type_name=True, body=mapping)

# with open('/Users/wanggang/Desktop/index.json', 'r', encoding='utf8') as fp:
#     json_data = json.load(fp)
#     for item in json_data:
#         print("item", item)
#         es.index(index="news",  doc_type='politics', document=item)
#     print('这是文件中的json数据：', json_data)
#     print('这是读取到文件数据的数据类型：', type(json_data))
