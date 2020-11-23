from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch(hosts="http://ggtaiwanmini.117503445.top:9200")

ACTIONS = []
#这个好像只会插入第一个
#似乎必须要带id
action1 ={
                    "_index": "clawer",
                    "_type": "videoMessage",
                   # "_id":"bSlegGUBmJ2C8ZCSC1R1",
                    "_source":{
                        "mime": "233qdsaasssq",
                        "file_size": 2,
                        "title": "hello kitty",
                        "content": "this is a hello kitty",
                        "file_url": "https:",
                        "author": "sandra",
                        "author_avatar": "https",
                        "create_time": "145",
                        "update_time": "789",
                        "thumbnail_url": "https:",
                        "website": "vimeo",
                        "process": 100
                    }
                }
action2 ={
                    "_index": "indes_test",
                    "_type": "videoMessage",
                    #"_id":"bSlegGUBmJ2C8ZCSC1R2",
                    "_source":{
                        "mime": "233q阿斯达aqasdsada",
                        "file_size": 2,
                        "title": "hello kitty",
                        "content": "this is a hello kitty",
                        "file_url": "https:",
                        "author": "sandra",
                        "author_avatar": "https",
                        "create_time": "122",
                        "update_time": "776",
                        "thumbnail_url": "https:",
                        "website": "vimeo",
                        "process": 100
                    }
                }

ACTIONS.append(action1)
ACTIONS.append(action2)

es.bulk(body=ACTIONS,index="clawer",doc_type="videoMessage")
