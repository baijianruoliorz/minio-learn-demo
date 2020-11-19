import time
from datetime import datetime
from minio import CopyConditions
from minio import Minio
from minio.error import ResponseError

# copy的一些条件  注意：本API支持的最大文件大小是5TB。

# 第一次运行报错 minio.error.PreconditionFailed: PreconditionFailed: message: At least one of the preconditions you specified did not hold.
# 不在copy_object函数加上最后一个参数就不报错了: copy_conditions,metadata=metadata
copy_conditions = CopyConditions()
# Set modified condition, copy object modified since 2014 April.
t = (2014, 4, 0, 0, 0, 0, 0, 0, 0)
mod_since = datetime.utcfromtimestamp(time.mktime(t))
copy_conditions.set_modified_since(mod_since)

# Set unmodified condition, copy object unmodified since 2014 April.
copy_conditions.set_unmodified_since(mod_since)

# Set matching ETag condition, copy object which matches the following ETag.
copy_conditions.set_match_etag("31624deb84149d2f8ef9c385918b653a")

# Set matching ETag except condition, copy object which does not match the following ETag.
copy_conditions.set_match_etag_except("31624deb84149d2f8ef9c385918b653a")

# Set metadata
metadata = {"test-key": "test-data"}

minioClient = Minio('ggtaiwanmini.117503445.top:9000',
                  access_key='admin',
                  secret_key='admin123',
                  secure=False)

try:
    copy_result = minioClient.copy_object("maylogs", "newcopy.txt",
                                          "/liqiqi/min-io.txt"
                                        )   #这里加不加最后一个参数有待讨论
    print(copy_result)
except ResponseError as err:
    print(err)