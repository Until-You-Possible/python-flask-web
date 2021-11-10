# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import uuid

from elasticsearch import Elasticsearch, helpers

# create a new instance of the Elasticsearch client class
elastic = Elasticsearch()
# ...or uncomment to use this instead:
# elastic = Elasticsearch("localhost")

'''
a simple function that gets the working path of
the Python script and returns it
'''


def script_path():
    path = os.path.dirname(os.path.realpath(__file__))
    if os.name == 'posix':  # posix is for macOS or Linux
        path = path + "/"
    else:
        path = path + chr(92)  # backslash is for Windows
    return path


'''
this function opens a file and returns its
contents as a list of strings split by linebreaks
'''


def get_data_from_file(self, path=script_path()):
    file = open(path + str(self), encoding="utf8", errors='ignore')
    data = [line.strip() for line in file]
    file.close()
    return data


'''
generator to push bulk data from a JSON
file into an Elasticsearch index
'''


def bulk_json_data(json_file, _index, doc_type):
    json_list = get_data_from_file(json_file)
    for doc in json_list:
        # use a `yield` generator so that the data
        # isn't loaded into memory
        if '{"index"' not in doc:
            yield {
                "_index": _index,
                "_type": doc_type,
                "_id": uuid.uuid4(),
                "_source": doc
            }


try:
    # make the bulk call, and get a response
    response = helpers.bulk(elastic, bulk_json_data("people.json", "employees", "people"))
    print("\nbulk_json_data() RESPONSE:", response)
except Exception as e:
    print("\nERROR:", e)

# iterator for a single document
actions = [
    {
        "_id": uuid.uuid4(),  # random UUID for _id
        "doc_type": "person",  # document _type
        "doc": {  # the body of the document
            "name": "George Peterson",
            "sex": "male",
            "age": 34,
            "years": 10
        }
    }
]

# iterator for multiple docs
actions = [
    {
        "_id": uuid.uuid4(),  # random UUID for _id
        "doc_type": "person",  # document _type
        "doc": {  # the body of the document
            "name": "George Peterson",
            "sex": "male",
            "age": 34 + doc,
            "years": 10 + doc
        }
    }
    for doc in range(100)  # use 'for' loop to insert 100 documents
]

try:
    # make the bulk call using 'actions' and get a response
    response = helpers.bulk(elastic, actions, index='employees', doc_type='people')
    print("\nactions RESPONSE:", response)
except Exception as e:
    print("\nERROR:", e)
