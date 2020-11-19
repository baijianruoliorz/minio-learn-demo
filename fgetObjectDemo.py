from minio import Minio


from minio.error import ResponseError
minioClient = Minio('ggtaiwanmini.117503445.top:9000',
                  access_key='admin',
                  secret_key='admin123',
                  secure=False)

# 下载文件保存到本地不太理解,,
# 如果保存的是文件夹 报错 :file is a directory.
# file is a directory.
try:
    print(minioClient.fget_object('liqiqi', 'min-io.txt', 'C://User//minioPythonDemo/1.txt'))
except ResponseError as err:
    print(err)