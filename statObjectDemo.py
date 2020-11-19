from minio import Minio


from minio.error import ResponseError
minioClient = Minio('ggtaiwanmini.117503445.top:9000',
                  access_key='admin',
                  secret_key='admin123',
                  secure=False)
# 获取对象的元数据。
try:
    print(minioClient.stat_object('liqiqi', 'min-io.txt'))
except ResponseError as err:
    print(err)
    #返回值大概是这些内容
    # g: cf2f245835d16dce38e75f2e7ed524ad
    # size: 1803
    # content_type: text / plain
    # is_dir: False
    # metadata: {'Content-Type': 'text/plain'g: cf2f245835d16dce38e75f2e7ed524ad size: 1803 content_type: text / plain
    #            is_dir: Falsemetadata: {
    #         'Content-Type': 'tg: cf2f245835d16dce38e75f2e7ed524ad size: 1803 content_type: text/plain is_dir: False metadata: {'
    #         Content - Type': 'text / pg: cf2f245835d16dce38e75f2e7ed524ad size: 1803 content_type: text / plain
    #         is_dir: False metadata: {'Content-Type': g: cf2f245835d16dce38e75f2e7ed524ad
    # size: 1803
    # content_type: text / plain
    # is_dir: False
    # metadata: {
    #     'Conteg: cf2f245835d16dce38e75f2e7ed524ad size: 1803 conteng: cf2f245835d16dce38e75f2e7ed524ad size: 1803 content_type: text/plain is_dir: False metadata: {'
    # Content - Type
    # ': '
    # text / plain
    # '} >
