from minio import Minio


from minio.error import ResponseError
minioClient = Minio('ggtaiwanmini.117503445.top:9000',
                  access_key='admin',
                  secret_key='admin123',
                  secure=False)
# 下载指定区间的对象字节数组
try:
    data = minioClient.get_partial_object('liqiqi', 'min-io.txt', 2, 4)
    # 下载后就在本目录的文件名称
    with open('my-testfile-2', 'wb') as file_data:
        for d in data:
            file_data.write(d)
except ResponseError as err:
    print(err)