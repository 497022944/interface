from Config.Log import *
from Config.LogBug import *

logbug = LogBug()
logger = Log()

class Public:
    @staticmethod
    def testxubao(self, StatusMessage):
        falg = True
        if StatusMessage == '续保成功':
            return falg
        else:
            logbug.debug("续保--异常信息为:{}".format(StatusMessage))
            return StatusMessage
    @staticmethod
    def testbaojia(self, baojiaStatusMessage):
        falg = True
        if baojiaStatusMessage == '请求发送成功':
            return falg
        else:
            logbug.debug("报价--异常信息为:{}".format(baojiaStatusMessage))
            return baojiaStatusMessage
