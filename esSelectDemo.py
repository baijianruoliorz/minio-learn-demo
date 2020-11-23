# coding:utf-8

# author:baijianruoliorz
import pandas as pd
from elasticsearch import Elasticsearch

# desk path：/Users/super/Desktop/
import dataFrameToJson

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

# 实例化对象
es = Elasticsearch(hosts="http://ggtaiwanmini.117503445.top:9200")

total_count = es.count(index="video")['count']

print('总数据量：', total_count)


query_json = {
    "query": {
        "bool": {
            "must": [
                {
                    "match_all": {

                    }
                }
            ],
        }
    }
}

data = es.search(index="video", body=query_json)


data = data["hits"]["hits"]


df = pd.DataFrame(data)



df = pd.DataFrame(list(df["_source"]))




print("df的type是:  ",type(df))




print(df)
print(dataFrameToJson.to_json2(df))
