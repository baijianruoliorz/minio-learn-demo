from minio import Minio
import os

from minio.error import ResponseError
# 添加一个新的对象到对象存储服务
# 单个对象的最大大小限制在5TB。put_object在对象大于5MiB时，
# 自动使用multiple parts方式上传。
# 这样，当上传失败时，客户端只需要上传未成功的部分即可
# （类似断点上传）。上传的对象使用MD5SUM签名进行完整性验证。
# 返回值 ('da4132f54c28b321d8231b20663b6a61', None)
# 执行了两个try 所以传了两次
minioClient = Minio('ggtaiwanmini.117503445.top:9000',
                  access_key='admin',
                  secret_key='admin123',
                  secure=False)
try:
    with open('putFileApiTestFile', 'rb') as file_data:   #要上传的file
        file_stat = os.stat('putFileApiTestFile')    #可以直接下成txt格式
        print(minioClient.put_object('liqiqi', 'putnefile.txt',
                               file_data, file_stat.st_size))
except ResponseError as err:
    print(err)

# Put a file with 'application/csv'.
try:
    with open('my-testfile.csv', 'rb') as file_data:
        file_stat = os.stat('my-testfile.csv')   #可以从本地找到
        minioClient.put_object('maylogs', 'newmyobject.csv', file_data,
                    file_stat.st_size, content_type='application/csv')
except ResponseError as err:
    print(err)