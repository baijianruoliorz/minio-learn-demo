from minio import Minio


from minio.error import ResponseError
minioClient = Minio('ggtaiwanmini.117503445.top:9000',
                  access_key='admin',
                  secret_key='admin123',
                  secure=False)


#通过文件上传到对象中。
# Put an object 'myobject' with contents from '/tmp/otherobject', upon success prints the etag identifier computed by server.
# fanhui ('0200eb05a5d0e2a77478699a9244a941', None)
# 这里上传了一张图片
try:
    print(minioClient.fput_object('liqiqi', 'myobjectsss.jpg', 'C://User//minioPythonDemo//test.jpg'))
except ResponseError as err:
    print(err)

# Put on object 'myobject.csv' with contents from
# '/tmp/otherobject.csv' as 'application/csv'.
# try:
#     print(minioClient.fput_object('mybucket', 'myobject.csv',
#                              '/tmp/otherobject.csv',
#                              content_type='application/csv'))
# except ResponseError as err:
#     print(err)