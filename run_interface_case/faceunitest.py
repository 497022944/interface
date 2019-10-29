import unittest, time, re, json
from Config.Log import *
from Config.LogBug import *
from Publicmethod.log_class import log_value
from Publicmethod.read_config import read_ini
from business_interface.facecase import Run_class
from Private_method.xianshang_method import xianshang_name
from Private_method.xianxia_method import xianxia_name

log_info_value = {}
log_bug_value = {}
logbug = LogBug()
logger = Log()
# 线上线下对比存储并且分类
jsondict = {
    '失败': {
        '线上对比失败': {},
        '线下对比失败': {}
    }
}
jsondict1 = {
    '成功': {
        '线上对比成功': {},
        '线下对比成功': {}
    }
}
jsondictxianshang = {}
jsondictxianxia = {}
jsondictchenggongx = {}
jsondictshibaix = {}
duibikey = []
xianshang = {}
xianxia = {}
keyfuzhi = []


class Run_case(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01case(self):
        global dictnew
        log = log_value()
        run_test_case = Run_class()
        read_con = read_ini()
        readagin = read_con.Read_ini_loading()
        secs = readagin.sections()  # 加载ini值
        Selecttheusecase1 = readagin.getint('Selecttheusecase', 'Selecttheusecase')
        if Selecttheusecase1 == 1:  # 商业+交强+车船
            run_test = run_test_case.test_02_Basic_double_coverage()
            run_test_sui = run_test_case.test_03_Basic_double_coverage()
        elif Selecttheusecase1 == 2:  # 单商业
            run_test = run_test_case.test_04_Basic_double_coverage()
            run_test_sui = run_test_case.test_03_Basic_double_coverage()
        elif Selecttheusecase1 == 3:  # 请求上线下线双险种对比
            xianshang_names = xianshang_name()
            xianshangdict = xianshang_names.xiashang_names()
            xianxia_names = xianxia_name()
            xianxiadict = xianxia_names.xiaxia_names()
            for k,v in xianshangdict.items():
                for k1, v1 in xianxiadict.items():
                    if k == k1:
                        jsondict1['成功']['线上对比成功'] = {}
                        jsondict1['成功']['线下对比成功'] = {}
                        jsondict['失败']['线上对比失败'] = {}
                        jsondict['失败']['线下对比失败'] = {}
                        keyfuzhi.clear()
                        for k2, v2 in v.items():
                            keyfuzhi.append(k2)
                        for key in keyfuzhi:
                            jsondictxianshang.clear()
                            jsondictxianxia.clear()
                            if key in v and key in v1 and v[key] in v1[key]:
                                jsondictxianshang[key] = v[key]
                                jsondictxianxia[key] = v1[key]
                                jsondict1['成功']['线上对比成功'].update(jsondictxianshang)
                                jsondict1['成功']['线下对比成功'].update(jsondictxianxia)
                            elif key in v and key in v1 and v[key] not in v1[key]:
                                jsondictxianshang[key] = v[key]
                                jsondictxianxia[key] = v1[key]
                                jsondict['失败']['线上对比失败'].update(jsondictxianshang)
                                jsondict['失败']['线下对比失败'].update(jsondictxianxia)
                            elif key in v and key not in v1:
                                jsondictxianshang[key] = v[key]
                                jsondict['失败']['线上对比失败'].update(jsondictxianshang)
                            elif key not in v and key in v1:
                                jsondictxianxia[key] = v1[key]
                                jsondict['失败']['线下对比失败'].update(jsondictxianxia)
                            else:
                                dictnews = json.dumps(jsondict, ensure_ascii=False, sort_keys=True, indent=2)
                                logbug.debug("日志记录:{}".format(dictnews))
                        dictnews1 = json.dumps(jsondict1, ensure_ascii=False, sort_keys=True, indent=2)
                        logger.info("日志记录---{}:{}".format(k,dictnews1))
                        dictnews = json.dumps(jsondict,ensure_ascii=False,sort_keys=True, indent=2)
                        logbug.debug("日志记录---{}:{}".format(k,dictnews))


                # run_test = run_test_case.test_05_Basic_double_coverage()
                # run_test_sui = run_test_case.test_03_Basic_double_coverage()


if __name__ == '__main__':
    unittest.main()
