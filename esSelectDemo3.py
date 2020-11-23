# coding:utf-8

# author:baijianruoliorz
import pandas as pd
from elasticsearch import Elasticsearch

# desk path：/Users/super/Desktop/

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

# 实例化对象
es = Elasticsearch(hosts="http://ggtaiwanmini.117503445.top:9200")

total_count = es.count(index="clawer")['count']

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
    },
    "sort": [
        {
            "process": {
                "order": "asc"
            }
        }
    ],
    "from": 4,  # 分页的两个参数 就是c:从第几个开始 l
    "size": 4
    #"from": 0,  # 分页的两个参数 就是c:从第几个开始 l
    #"size": 1
}
#实锤了.这个只能是int long 类型字段才能排序
data = es.search(index="clawer", body=query_json)


data = data["hits"]["hits"]


df = pd.DataFrame(data)



df = pd.DataFrame(list(df["_source"]))

df = df[["create_time", "mime", "process"]]
print("df的type是:  ",type(df))
print(df)

