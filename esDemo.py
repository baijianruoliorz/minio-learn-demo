# coding:utf-8

# author:baijianruoliorz
import os
import dataFrameToJson
import pandas as pd
from elasticsearch import Elasticsearch

# desk path：/Users/super/Desktop/

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

# 实例化对象
es = Elasticsearch(hosts="http://ggtaiwanmini.117503445.top:9200")
# 就是elasticsearch里的数据库名称(可以这么理解)       count:读出这个index里的全部对象数量
total_count = es.count(index="video")['count']

print('总数据量：', total_count)

print(os.getcwd())
query_json = {
    "query": {
        "match_all": {},
    },"size": 10
}
#查询到数据
data = es.search(index="video", body=query_json)

#print(data)
#exit()
# 去字典的方式来取出数据
data = data["hits"]["hits"]

#print(data)
#exit()
#elasticsearch里面不是关系型数据库 所以要转一下
# 这样就可以转成关系型数据库
df = pd.DataFrame(data)

#print(df)
#exit()

df = pd.DataFrame(list(df["_source"]))

#print(df)
#exit()
# 取出一些特定的字段
df = df[["file_size", "mime", "content", "author","create_time"]]

#    file_size         mime                content  author
# 0          2       233qaq  this is a hello kitty  sandra
# 1          2       233qaq  this is a hello kitty  sandra
# 2          2       233qaq  this is a hello kitty  sandra
# 3          2  233qasadasq  this is a hello kitty  sandra
print("df的type是:  ",type(df))

#具体见这篇博客 :https://blog.csdn.net/wanglingli95/article/details/78887771

#下面是返回content列的操作
#print(df["content"])
print("YXR---ORZ")
#df type :pandas.core.frame.DataFrame
#下面是返回第二行的操作
#1    this is a hello kitty
print(df[1:2]["content"])
print("获取ID的方法")
#下面是返回第二行 content 和 mime列的操作 这个好像有错误
#print(df[1:2,['content','mime']])

#返回第二行第二列:  可以直接取到 233qaq 这个值啦 然后下面就是依次返回的信息
#重要!
print("SADAS",df.iat[1,1],df.iat[1,2],df.iat[1,3])
#下面两个的查询结果 分别是 create_time 和 process的类型
# <class 'str'>
# <class 'numpy.int64'>


#选择2-4行第1,3列的位置
print("QAQ")

#print(df.ix[1:2,[0,2]])
print()
#展示全部
print(df)
print(dataFrameToJson.to_json2(df))

# es默认展示10条数据 如果想要更多 只需要改成 "size":20这样就是二十条了,即 query_json
#df.to_excel("D://XDUProject//es.xlsx", index=False)

#print('\n')

#print(df.info())