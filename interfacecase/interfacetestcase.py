import unittest
import json
from Interface.Camera import *
from Config.Log import *
from Config.LogBug import *
from interfacecase.public import Public
from time import sleep
import time

#读取txt车牌数据
yongli_path = os.path.dirname(os.path.abspath('.')) + "\chepai\chepaiku.txt"
# txt文件第一行一个符号调试 sig
ele = open(yongli_path, 'r', encoding='utf-8-sig')

#选择保险公司
baoxiangongsi = 4
chenggonglv = ["成功车牌"]
baojiashibai = ["失败车牌"]
#引入log文件
logger = Log()
logbug = LogBug()

class TestMethod(unittest.TestCase):

    def test01(self):
        a = ele.readlines()
        # driver = webdriver.Chrome()
        for data in a:
            name = data.strip('\t\r\n')
            name_f = name[0:1:1]
            cict = name_f
            if name_f == "粤":
                cict = 14
                logger.info("您选择得城市为广州")
            elif name_f == "苏":
                cict = 8
                logger.info("您选择得城市为南京")
            elif name_f == "京":
                cict = 1
                logger.info("您选择得城市为北京")
            elif name_f == "冀":
                cict = 12
                logger.info("您选择得城市为石家庄")
            elif name_f == "渝":
                cict = 2
                logger.info("您选择得城市为重庆")
            else:
                logbug.debug("车牌号"+name+"您选择的城市尚未开发，请重新选择车牌")
            #续保地址请求
            url = 'http://it.91bihu.me/api/CarInsurance/getreinfo'
            data = {
                            'LicenseNo': name,
                            'CityCode': cict,
                            'CanShowExhaustScale': '1',
                            'CanShowNo': '1',
                            'ChildAgent': '191260',
                            'Agent': '191260',
                            'Group': '1',
                            'RenewalCarType': '0',
                            'RenewalSource': '0',
                            'RenewalType': '4',
                            'ShowAutoMoldCode': '1',
                            'ShowBaoFei': '1',
                            'ShowFybc': '1',
                            'ShowInnerInfo': '1',
                            'ShowPACheckCode': '1',
                            'ShowRelation': '1',
                            'ShowRenewalCarType': '1',
                            'ShowSanZheJieJiaRi': '1',
                            'ShowSheBei': '1',
                            'ShowTransferModel': '1',
                            'ShowXiuLiChangType': '1',
                            'TimeFormat': '1',
                            'CustKey': '4DE9B7822E0DE81FC734BC5689AB6F03',
                            'SecCode': '23c73b3be4c698971dbf320699431545',

                    }
            xubao = RunMain(url, 'GET', data)
            logger.info(xubao.res)

            if xubao.res == "您对同一辆车的请求过于频繁，请稍候再试":
                logbug.debug("车牌号"+name+"续保内容为:"+xubao.res+"!!")
                continue

            # 递归
            # 获取字典中的objkey对应的值，适用于字典嵌套
            # dict:字典
            # objkey:目标key
            # default:找不到时返回的默认值"""\
            def dict_get(dict1, objkey, default=None):
                for k, v in dict1.items():
                    if k == objkey:
                        return v
                    else:
                        if type(v) is dict:
                            ret = dict_get(v, objkey)
                            if ret is not default:
                                return ret
            #续保返回结果
            StatusMessage = (xubao.res["StatusMessage"])
            NewStatusMessage = Public.testxubao(self, StatusMessage=StatusMessage)

            #StatusMessage返回值是否为续保成功
            if NewStatusMessage == True:
                logger.info("是--续保成功车牌为:{}" .format(name))
            else:
                logbug.debug("否--续保成功即将执行下一辆--车牌为:{}".format(name))
                continue

            #车牌号
            LicenseNo = dict_get(xubao.res, 'LicenseNo')
            logger.info("续保返回车牌号为: %s" % LicenseNo)
            try:
                if LicenseNo == name:
                    logger.info("续保车牌号与上传车牌号一致:{}".format(LicenseNo))
                else:
                    logbug.debug("您续保得车牌与上传车牌有差异你搞啥呢！即将执行下一辆！ %s" % LicenseNo)
                    continue
            except AssertionError as e:
                logbug.debug("您续保得车牌与上传车牌有差异你搞啥呢！即将执行下一辆！ %s" % LicenseNo)
            # 使用性质
            # 1：家庭自用车（默认），
            # 2：党政机关、事业团体，
            # 3：非营业企业客车，
            # 4：不区分营业非营业（仅支持人保报价），
            # 5：出租租赁（仅支持人保报价），
            # 6：营业货车（仅支持人保报价），
            # 7：非营业货车（仅支持人保报价）
            # 8: 城市公交
            CarUsedType = dict_get(xubao.res, 'CarUsedType')
            logger.info("续保返回使用性质为: %s" % CarUsedType)
            #证件类型
            IdType = dict_get(xubao.res, 'IdType')
            logger.info("续保返回证件类型为: %s" % IdType)
            #证件号被保人
            InsuredIdCard = dict_get(xubao.res, 'InsuredIdCard')
            logger.info("续保返回证件类型为: %s" % InsuredIdCard)
            #证件类型被保人
            InsuredIdType = dict_get(xubao.res, 'InsuredIdType')
            logger.info("续保返回证件类型为: %s" % InsuredIdType)
            #车主姓名
            LicenseOw = dict_get(xubao.res, 'LicenseOwner')
            logger.info("续保返回车主姓名为: %s" % LicenseOw)
            try:
                if InsuredIdType == 1:
                    logger.info("您的续保证件类型为暂不处理: %s" % IdType)
                    if LicenseOw == None:
                        LicenseOwners = '叶星辰'
                        LicenseOw = LicenseOwners
                        logbug.debug("车牌号"+LicenseNo+"您的续保返回值车主为空，我已经赋值为: %s" % LicenseOw)
                    elif InsuredIdCard == None:
                        IdCard1 = '110225196106170085'
                        InsuredIdCard = IdCard1
                        logbug.debug("车牌号"+LicenseNo+"您的续保返回值车主证件号为空，我已经赋值为: %s" % IdCard1)
                    else:
                        logger.info("您的续保返回值证件类型为: %s" % LicenseOw)
                elif IdType == 2:
                    logger.info("您的续保证件类型为: %s" % IdType)
                    if LicenseOw == None:
                        LicenseOwners = '北京长阳建业建筑工程有限公司'
                        LicenseOw = LicenseOwners
                        logbug.debug("车牌号"+LicenseNo+"您的续保返回值车主为空，我已经赋值为: %s" % LicenseOw)
                    elif InsuredIdCard == None:
                        IdCard1 = '79344156-9'
                        InsuredIdCard = IdCard1
                        logbug.debug("车牌号"+LicenseNo+"您的续保返回值车主证件号为空，我已经赋值为: %s" % IdCard1)
                    else:
                        logger.info("您的续保返回值被保人证件类型为: %s" % LicenseOw)
                else:
                    logger.info("您的续保返回值被保人为: %s" % LicenseOw)

            except AssertionError as e:
                logbug.debug("车牌号"+LicenseNo+"您的续保返回值车主为！ %s" % LicenseOw)
            #被保人姓名
            InsuredName = dict_get(xubao.res, 'InsuredName')
            logger.info("续保返回被保人姓名为: %s" % InsuredName)
            #新车购置价
            PurchasePrice = dict_get(xubao.res, 'PurchasePrice')
            logger.info("续保返回新车购置价为: %s" % PurchasePrice)
            #证件类型
            # 0：没有取到
            # 1：身份证
            # 2：组织机构代码证
            # 3：护照
            # 4：军官证
            # 5：港澳居民来往内地通行证
            # 6：其他
            # 7：港澳通行证
            # 8：出生证
            # 9：营业执照（社会统一信用代码）
            # 10：税务登记证
            # 11：驾驶证
            # 12：营业执照（区别与9，这是三证合一之前的）
            # 13：台胞证
            # 14：港澳身份证

            #城市id
            CityCode = dict_get(xubao.res, 'CityCode')
            logger.info("续保返回城市id为: %s" % CityCode)
            #发动机号码
            EngineNo = dict_get(xubao.res, 'EngineNo')
            logger.info("续保返回发动机号码为: %s" % EngineNo)

            #品牌型号
            ModleName = dict_get(xubao.res, 'ModleName')
            logger.info("续保返回品牌型号为: %s" % ModleName)

            #车辆注册日期
            RegisterDate = dict_get(xubao.res, 'RegisterDate')
            logger.info("续保返回车辆注册日期为: %s" % RegisterDate)

            #车架号
            CarVin = dict_get(xubao.res, 'CarVin')
            logger.info("续保返回车架号为: %s" % CarVin)

            #交强险到期时间
            ForceExpireDate = dict_get(xubao.res, 'ForceExpireDate')
            logger.info("续保返回交强险到期时间为: %s" % ForceExpireDate)

            #商业险到期时间
            BusinessExpireDate = dict_get(xubao.res, 'BusinessExpireDate')
            logger.info("续保返回商业险到期时间为: %s" % BusinessExpireDate)
            try:
                if ForceExpireDate == '' and BusinessExpireDate == '':
                    logger.info("续保返回值上年投保为双险种 %s" % ForceExpireDate+BusinessExpireDate)
                elif ForceExpireDate == '':
                    logger.info("续保返回值上年投保为单商业 %s" % BusinessExpireDate)
                elif BusinessExpireDate == '':
                    logger.info("续保返回值上年投保为单交强 %s" % ForceExpireDate)
                else:
                    logger.info("续保返回值上年投保为双险种 %s" % ForceExpireDate+BusinessExpireDate)
            except AssertionError as e:
                logbug.debug("车牌号"+LicenseNo+"您续保得续保返回值上年投保有差异你搞啥呢！即将执行下一辆！ %s" % ForceExpireDate+BusinessExpireDate)
                continue
            #下年的交强起保日期
            NextForceStartDate = dict_get(xubao.res, 'NextForceStartDate')
            logger.info("续保返回下年的交强起保日期为: %s" % NextForceStartDate)

            #下年的商业起保日期
            NextBusinessStartDate = dict_get(xubao.res, 'NextBusinessStartDate')
            logger.info("续保返回下年的商业起保日期为: %s" % NextBusinessStartDate)

            #座位数量
            SeatCount = dict_get(xubao.res, 'SeatCount')
            logger.info("续保返回座位数量为: %s" % SeatCount)

            #商业险保单号
            BizNo = dict_get(xubao.res, 'BizNo')
            logger.info("续保返回商业险保单号为: %s" % BizNo)

            #交强险保单号
            ForceNo = dict_get(xubao.res, 'ForceNo')
            logger.info("续保返回交强险保单号为: %s" % ForceNo)

            #上年保险公司的枚举值，请参考上面保险资源枚举列表
            Source = dict_get(xubao.res, 'Source')
            logger.info("续保返回上年保险公司的枚举值: %s" % Source)
            try:
                if Source == -1:
                    logbug.debug("车牌号"+LicenseNo+"续保的上年投保公司都是-1了还不赶紧提bug.... %s" % Source)
                    continue
                else:
                    logger.info("续保返回值上年投保公司为: %s" % Source)
            except AssertionError as e:
                logbug.debug("车牌号"+LicenseNo+"您续保得续保返回值上年投保公司有差异你搞啥呢！即将执行下一辆！ %s" % Source)
                continue

            #报价请求
            try:
                if StatusMessage == "续保成功":
                    #保险公司读取txt转换
                        dat = baoxiangongsi
                        url1 = 'http://it.91bihu.me/api/CarInsurance/PostPrecisePrice'
                        data1 = {
                                'LicenseNo': LicenseNo,
                                'CityCode': CityCode,
                                'Agent': '191260',
                                'ForceTax': '1',
                                'IsPublic': '0',
                                'BuJiMianCheSun': '1',
                                'BuJiMianSanZhe': '1',
                                'SiJi': '10000',
                                'ChengKe': '10000',
                                'CheSun': '1',
                                'SanZhe': '500000',
                                'CustKey': 'hehaitaohh',
                                'SecCode': 'e9779d2c054d69306fc9fc0b93bfa8a9',
                                'BuJiMianChengKe': '1',
                                'CarOwnersName': LicenseOw,
                                'OwnerIdCardType': InsuredIdType,
                                'IdCard': InsuredIdCard,
                                'InsuredName': LicenseOw,
                                'InsuredIdType': InsuredIdType,
                                'InsuredIdCard': InsuredIdCard,
                                'HolderName': LicenseOw,
                                'HolderIdType': InsuredIdType,
                                'HolderIdCard': InsuredIdCard,
                                'BuJiMianRenYuan': '1',
                                'QuoteGroup': dat,
                                'SubmitGroup': '0',
                                'IsTempStorage': '1',

                                }
                        start = time.time()
                        baojia = RunMain(url1, 'GET', data1)
                        end = time.time()
                        logbug.debug('Running time: %s Seconds'%(end-start))
                        logger.info(baojia.res)

                        #报价请求
                        StatusMessagee = (baojia.res["StatusMessage"])
                        Newbaojia = Public.testbaojia(self, baojiaStatusMessage=StatusMessagee)
                        time.sleep(30)
                        try:
                            if Newbaojia != True:
                                break
                            else:
                                logger.info("报价请求发送显示: %s" % StatusMessagee)
                                url2 = 'http://qa.interfaces.com/api/CarInsurance/GetPrecisePrice'
                                data2 = {
                                        'LicenseNo': LicenseNo,
                                        'Agent': '17295',
                                        'CustKey': 'hehaitaohh',
                                        'SecCode': 'e9779d2c054d69306fc9fc0b93bfa8a9',
                                        'TimeFormat': '1',
                                        'ShowEmail': '1',
                                        'QuoteGroup': dat,
                                        'SubmitGroup': '0',
                                        'IsTempStorage': '1',

                                        }
                                baojiajg = RunMain(url2, 'GET', data2)
                                logger.info(baojiajg.res)
                                StatusMessageeee = (baojiajg.res["StatusMessage"])
                                try:
                                    if StatusMessageeee == "获取报价信息成功":
                                        QuoteResultt = dict_get(baojiajg.res, 'QuoteResult')
                                        QuoteStatuss = dict_get(baojiajg.res, 'QuoteStatus')
                                        #QuoteStatuss报价状态，-1=未报价， 0=报价失败，>0报价成功   QuoteResultt报价信息。（备注字符最大长度：1000）
                                        if QuoteStatuss == -1:
                                            logbug.debug("车牌号"+LicenseNo+"你的报价结果显示是: %s" % QuoteStatuss+QuoteResultt,)
                                            baojiashibai.append(LicenseNo)
                                            #删除列表下标第0个
                                            #del chenggonglv[0]
                                            logbug.debug(baojiashibai)
                                        elif QuoteStatuss == 0:
                                            logbug.debug("车牌号"+LicenseNo+"你的报价结果显示是: %s" % QuoteStatuss+QuoteResultt,)
                                            baojiashibai.append(LicenseNo)
                                            #删除列表下标第0个
                                            #del chenggonglv[0]
                                            logbug.debug(baojiashibai)
                                        elif QuoteStatuss > 0:
                                            logbug.debug("车牌号"+LicenseNo+"你的报价结果显示是: %s" % QuoteStatuss+QuoteResultt,)
                                            chenggonglv.append(LicenseNo)
                                            logbug.debug(chenggonglv)
                                        else:
                                            logbug.debug("车牌号"+LicenseNo+"你的报价结果显示是什么乱七八糟: %s" % QuoteStatuss+QuoteResultt,)
                                            baojiashibai.append(LicenseNo)
                                            #删除列表下标第0个
                                            #del chenggonglv[0]
                                            logbug.debug(baojiashibai)

                                    else:
                                        logbug.debug("车牌号"+LicenseNo+"你的报价结果返回为: %s" % StatusMessageeee)
                                except AssertionError as e:
                                    logbug.debug("车牌号"+LicenseNo+"你的报价结果返回为: %s" % StatusMessageeee)


                        except AssertionError as e:
                            logbug.debug("车牌号"+LicenseNo)

                else:
                    logbug.debug("车牌号"+LicenseNo+"快看你的续保返回值状态显示: %s" % StatusMessage)
                    continue
            except AssertionError as e:
                logbug.debug("车牌号"+LicenseNo)







if __name__ == '__main__':
    unittest.main()
