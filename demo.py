from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)

from minio.error import ResponseError

minioClient = Minio('ggtaiwanmini.117503445.top:9000',
                  access_key='admin',
                  secret_key='admin123',
                  secure=False)
# 调用make_bucket来创建一个存储桶。
# maylogs就是创建的桶
try:
       minioClient.make_bucket("maylogs", location="us-east-1")
except BucketAlreadyOwnedByYou as err:
       pass
except BucketAlreadyExists as err:
       pass
except ResponseError as err:
       raise
else:
        try:
               minioClient.fput_object('maylogs', 'pumaserver_debug.log', 'C://User//minioPythonDemo//pumaserver_debug.log')
        except ResponseError as err:
               print(err)