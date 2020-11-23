from elasticsearch import Elasticsearch

es = Elasticsearch(hosts="http://ggtaiwanmini.117503445.top:9200")

action ={
    "mime": "233qaqssss",
    "file_size": 6,
    "title": "hello kittsady",
    "content": "this is a hello kitty",
    "file_url": "https:",
    "author": "sandra",
    "author_avatar": "https",
    "create_time": "1605731233",
    "update_time": "160576691111",
    "thumbnail_url": "https:",
    "website": "vimeoss",
    "process": 100
                }
#没有指定ID 就会瞎JB搞一个字母组成的ID给你
es.index(index="clawer",doc_type="videoMessage",body = action)
