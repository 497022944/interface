from Config.Log import *
from Config.LogBug import *

logbug = LogBug()
logger = Log()

class log_value:

    #info类调用
    @staticmethod
    def log_info(self, current_entry):
        logger.info("日志记录:{}".format(current_entry))
        current_entry.clear()

    #bug类调用
    @staticmethod
    def log_bug(self, current_entry_bug):
        logbug.debug("日志记录:{}".format(current_entry_bug))
        current_entry_bug.clear()