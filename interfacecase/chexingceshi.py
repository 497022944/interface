import unittest
import json
from Interface.Camera import *
from Config.Log import *
from Config.LogBug import *
from interfacecase.public import Public
from time import sleep
import time

baoxiangongshi = [1, 2, 4, 8]

#引入log文件
logger = Log()
logbug = LogBug()
yongli_path = os.path.dirname(os.path.abspath('.'))+"\chepai\chepaiku.txt"
ele = open(yongli_path, 'r', encoding='utf-8-sig')

yongli_path1 = os.path.dirname(os.path.abspath('.'))+"\chepai\chexing.txt"
ele1 = open(yongli_path1, 'r', encoding='utf-8')


class Chexingceshi(unittest.TestCase):

    def test01(self):
        chepai = ele.readlines()
        for chepaihao in chepai:
            chexing = ele1.readline()
            licenseno = chepaihao.strip('\t\r\n')
            name_f = licenseno[0:1:1]
            cict = name_f
            if name_f == "粤":
                cict = 14
                logger.info("您选择得城市为广州")
            elif name_f == "苏":
                cict = 8
                logger.info("您选择得城市为南京")
            elif name_f == "京":
                cict = 1
                logger.info("您选择得城市为北京{}".format(cict))
            elif name_f == "冀":
                cict = 12
                logger.info("您选择得城市为石家庄")
            elif name_f == "渝":
                cict = 2
                logger.info("您选择得城市为重庆")
            else:
                logbug.debug("车牌号"+licenseno+"您选择的城市尚未开发，请重新选择车牌")
            chexingqinqiu = chexing.strip('\r\n\t')
            lenchexing = len(chexingqinqiu)
            if lenchexing < 10:
                pingpai = chexingqinqiu
                lenchexing = lenchexing -1
            else:
                break
            for baoxiangongshixuanzhe in baoxiangongshi:
                gongshi = baoxiangongshixuanzhe
                #url = 'http://qa.interfaces.com/api/CarInsurance/GetNewVehicleInfo?'
                url = 'http://it.91bihu.me/api/CarInsurance/GetNewVehicleInfo?'
                data = {
                            'LicenseNo': licenseno,
                            'CityCode': cict,
                            'CarType': '1',
                            #'Source': gongshi,#gongshi
                            'IsNeedCarVin': '0',
                            'Agent': '191260',
                            'MoldName': pingpai,
                            'CustKey': '4DE9B7822E0DE81FC734BC5689AB6F03',
                            'SecCode': '23c73b3be4c698971dbf320699431545',

                    }
                #车型地址请求
                chexingqingqiu = RunMain(url, 'GET', data)
                che = chexingqingqiu.res["Items"]
                #返回的字典进行json转码 乱码输入ensure_ascii=False
                chejieguo = json.dumps(che, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '), )
                if chexingqingqiu.res["StatusMessage"] == '获取成功':
                    logger.info("车牌为:{}--车型为:{}--保险公司为:{}--您的结果为:{}--".format(licenseno, chexing, baoxiangongshixuanzhe, chexingqingqiu.res["StatusMessage"]))
                    logger.info("车型结果:{}".format(chejieguo))
                else:
                    logbug.debug("您的车型结果显示**{}**为异常".format(chexingqingqiu.res["StatusMessage"]))

if __name__ == '__main__':
    unittest.main()
