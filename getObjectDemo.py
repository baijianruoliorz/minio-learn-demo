from minio import Minio


from minio.error import ResponseError
minioClient = Minio('ggtaiwanmini.117503445.top:9000',
                  access_key='admin',
                  secret_key='admin123',
                  secure=False)

try:
    data = minioClient.get_object('liqiqi', 'min-io.txt')
    # 下载完成后的文件名  就叫 my-testfile 这里会把min-io.txt的内容下载到里面
    with open('my-testfile', 'wb') as file_data:
        for d in data.stream(32*1024):
            file_data.write(d)
except ResponseError as err:
    print(err)