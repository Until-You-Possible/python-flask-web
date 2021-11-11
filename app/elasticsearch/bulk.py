import json
import time

from elasticsearch import helpers

from elasticsearch import Elasticsearch

es_url = "http://127.0.0.1:9200"
es = Elasticsearch(es_url)
print(es.info)

configurations = {
    "index_name": "index_name",
    "index_type": "index_type",
    "request_body": {}
}

source_path = "/Users/wanggang/Documents/kba/kba.json"


def create_index():
    es.indices.create(index=configurations.get("index_name"), body=configurations.get("request_body"))
    print("create a new index")


# create_index()


def check_json_count():
    count = 0
    start_time = time.time()
    with open(source_path, "r", encoding="UTF-8") as fp:
        json_data = json.load(fp, strict=False)
        for item in json_data:
            count += 1
    end_time = time.time()
    t = end_time - start_time
    des = "读取这些数据{}条，共花费{}秒".format(count, t)
    return des


print(check_json_count())


def read_json_file():
    with open(source_path, "r", encoding="UTF-8") as fp:
        json_data = json.load(fp, strict=False)
        actions = []
        count = 0
        for item in json_data:
            count += 1
            action = {
                "_index": configurations.get("index_name"),
                "type": configurations.get("index_type"),
                "_source": item
            }
            actions.append(action)
            if len(actions) == 1000:
                helpers.bulk(es, actions)
                actions = []
    helpers.bulk(es, actions)


# read_json_file()


def check_json_count_block():
    count = 0
    block_size = 1024 * 8
    with open(source_path, "r", encoding="UTF-8") as fp:
        while True:
            chunk = fp.read(block_size)
            if not chunk:
                break
            count += chunk.count("SAP")
    return count


print("test number", check_json_count_block())














