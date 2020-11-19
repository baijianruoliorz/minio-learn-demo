from minio import Minio

from datetime import timedelta
from minio.error import ResponseError
#presigned URL可以有一个过期时间，默认是7天
minioClient = Minio('ggtaiwanmini.117503445.top:9000',
                  access_key='admin',
                  secret_key='admin123',
                  secure=False)
# presigned get object URL for object name, expires in 2 days.
try:
    print(minioClient.presigned_get_object('liqiqi', 'min-io.txt', expires=timedelta(days=2)))
# Response error is still possible since internally presigned does get bucket location.
except ResponseError as err:
    print(err)

# http://ggtaiwanmini.117503445.top:9000/liqiqi/min-io.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=admin
# %2F20201119%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201119T093439Z&X-Amz-Expires=172800&X-Amz-SignedHeaders
# =host&X-Amz-Signature=0218d888283955572be524079298bb78c3db6d94fa6b52ee30beb406e4e4c830
