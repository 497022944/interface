import re
import time
import unittest
from Config.Log import *
from Config.LogBug import *
from Interface.Camera import *
from Publicmethod.log_class import log_value
from Publicmethod.common_return import common_return_value
from Publicmethod.read_file import Read_file
from Publicmethod.read_config import read_ini
log_info_value = {}
log_bug_value = {}
success = []
dictchepai = {}
defeated = []
licenseNo111 = 0
InsuredName1 = '张鸣'
PostedName1 = '张鸣'
LicenseOwner1 = '张鸣'
HolderIdCard1 = '430219198106274665'
CredentislasNum1 = '430219198106274665'
InsuredIdCard1 = '430219198106274665'
IdType1 = 2
HolderIdType1 = 2
InsuredIdType1 = 2
xianxiabaojiajieguo = {}
xianxiabaojiajieguo1 = {}
class xianxia_name:
    def xiaxia_names(self):
        common_return = common_return_value()
        log = log_value()
        read_con = read_ini()
        readagin = read_con.Read_ini_loading()
        secs = readagin.sections()  # 加载ini值
        # licenseNo = readagin.get("LicenseNo", "licenseNo")
        file_path = os.path.dirname(os.path.abspath('.')) + '\Config\chepai.txt'
        conname = open(file_path, 'r', encoding='utf-8-sig')
        licenseNo1 = conname.readlines()
        global licenseNo1global
        licenseNo1global = int(len(licenseNo1))
        cict = str(readagin.get("Forcity", "cict"))
        cict1 = cict.split(',')
        nu1m = len(licenseNo1) / len(cict1)
        num = round(nu1m)
        insurance = readagin.getint("Theinsurancecompany", "insurance")
        Online = readagin.getint("Onlineoroffline", "Online")
        Agent = readagin.getint("Agent", "Agentx")

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
        log_info_value.update(请求='--------------线下请求--------------')
        log.log_info(self, current_entry=log_info_value)
        for i in range(len(cict1)):
            for j in range(i * num, num * (i + 1)):
                licenseNO = licenseNo1[j].strip('\r\n\t')
                xianxiabaojiajieguo[licenseNO] = [licenseNO]
                xianxiabaojiajieguo1.clear()
                cict = cict1[i]
                # print(licenseNO)
                log_info_value.update(选择城市=cict1[i], 车牌号=licenseNO)
                log.log_bug(self, log_info_value)
                url = 'http://qa.interfaces.com/api/CarInsurance/getreinfo?'
                data = {
                    'LicenseNo': licenseNO,
                    'CityCode': cict,
                    'Agent': Agent,
                    'Group': '1',
                    'CustKey': '4DE9B7822E0DE81FC734BC5689AB6F03',
                    'SecCode': '23c73b3be4c698971dbf320699431545',
                }
                if len(licenseNO) > 12 and len(licenseNO) < 18:
                    data['CarVin'] = data.pop('LicenseNo')
                    data1 = json.dumps(data)
                    start = time.time()
                    xubao = RunMain(url, 'GET', data)
                    end = time.time()
                    xubaovalues = int(end - start)
                    StatusMessage = xubao.res["StatusMessage"]
                    log_info_value.update(结果=StatusMessage)
                    common_return_a = common_return.testxubao(self, StatusMessage)
                    xianxiabaojiajieguo1['车牌'] = licenseNO
                    xianxiabaojiajieguo1['续保结果'] = StatusMessage
                    xianxiabaojiajieguo[licenseNO] = xianxiabaojiajieguo1.copy()
                elif len(licenseNO) < 12:
                    start = time.time()
                    xubao = RunMain(url, 'GET', data)
                    end = time.time()
                    xubaovalues = int(end - start)
                    StatusMessage = xubao.res["StatusMessage"]
                    log_info_value.update(结果=StatusMessage)
                    common_return_a = common_return.testxubao(self, StatusMessage)
                    xianxiabaojiajieguo1['车牌'] = licenseNO
                    xianxiabaojiajieguo1['续保结果'] = StatusMessage
                    xianxiabaojiajieguo[licenseNO] = xianxiabaojiajieguo1.copy()
                if common_return_a == True:
                    LicenseOwner3 = xubao.res['UserInfo']['LicenseOwner']
                    IdType3 = xubao.res['UserInfo']['IdType']
                    CredentislasNum3 = xubao.res['UserInfo']['CredentislasNum']
                    PostedName3 = xubao.res['UserInfo']['PostedName']
                    HolderIdType3 = xubao.res['UserInfo']['HolderIdType']
                    HolderIdCard3 = xubao.res['UserInfo']['HolderIdCard']
                    InsuredName3 = xubao.res['UserInfo']['InsuredName']
                    InsuredIdType3 = xubao.res['UserInfo']['InsuredIdType']
                    InsuredIdCard3 = xubao.res['UserInfo']['InsuredIdCard']
                    IsPublic = xubao.res['UserInfo']['IsPublic']
                    personnel = {}
                    personnel.update(LicenseOwner=LicenseOwner3, IdType=IdType3, CredentislasNum=CredentislasNum3,
                                     PostedName=PostedName3, HolderIdType=HolderIdType3, HolderIdCard=HolderIdCard3,
                                     InsuredName=InsuredName3, InsuredIdType=InsuredIdType3, InsuredIdCard=InsuredIdCard3)
                    print(personnel.items())
                    for k, item in personnel.items():
                        if IsPublic == 2:
                            if k == 'LicenseOwner':
                                if item == '' or item == 0:
                                    personnel.update(LicenseOwner='叶星辰')
                                elif '*' in item:
                                    personnel.update(LicenseOwner='叶星辰')
                            elif k == 'IdType':
                                if item == '' or item == 0:
                                    personnel.update(IdType=1)
                            elif k == 'CredentislasNum':
                                if item == '' or item == 0:
                                    personnel.update(CredentislasNum=430219198106274665)
                                elif '*' in item:
                                    personnel.update(CredentislasNum=430219198106274665)
                            elif k == 'PostedName':
                                if item == '' or item == 0:
                                    personnel.update(PostedName='叶星辰')
                                elif '*' in item:
                                    personnel.update(PostedName='叶星辰')
                            elif k == 'HolderIdType':
                                if item == '' or item == 0:
                                    personnel.update(HolderIdType=1)
                            elif k == 'HolderIdCard':
                                if item == '' or item == 0:
                                    personnel.update(HolderIdCard=430219198106274665)
                                elif '*' in item:
                                    personnel.update(HolderIdCard=430219198106274665)
                            elif k == 'InsuredName':
                                if item == '' or item == 0:
                                    personnel.update(InsuredName='叶星辰')
                                elif '*' in item:
                                    personnel.update(InsuredName='叶星辰')
                            elif k == 'InsuredIdType':
                                if item == '' or item == 0:
                                    personnel.update(InsuredIdType=1)
                            elif k == 'InsuredIdCard':
                                if item == '' or item == 0:
                                    personnel.update(InsuredIdCard=430219198106274665)
                                elif '*' in item:
                                    personnel.update(InsuredIdCard=430219198106274665)
                            else:
                                log_info_value.update(无变化关系人=personnel)
                                log.log_info(self, log_info_value)
                        elif IsPublic == 1:
                            if k == 'LicenseOwner':
                                if item == '' or item == 0:
                                    personnel.update(LicenseOwner='壁虎科技有限公司')
                                elif '*' in item:
                                    personnel.update(LicenseOwner='壁虎科技有限公司')
                            elif k == 'IdType':
                                if item == '' or item == 0 or item == 1:
                                    personnel.update(InsuredIdType=2)
                            elif k == 'CredentislasNum':
                                if item == '' or item == 0 or len(item) <= 15:
                                    personnel.update(CredentislasNum=740054610)
                                elif '*' in item:
                                    personnel.update(CredentislasNum=740054610)
                            elif k == 'PostedName':
                                if item == '' or item == 0:
                                    personnel.update(PostedName='壁虎科技有限公司')
                                elif '*' in item:
                                    personnel.update(PostedName='壁虎科技有限公司')
                            elif k == 'HolderIdType':
                                if item == '' or item == 0 or item == 1:
                                    personnel.update(InsuredIdType=2)
                            elif k == 'HolderIdCard':
                                if item == '' or item == 0 or len(item) <= 15:
                                    personnel.update(HolderIdCard=740054610)
                                elif '*' in item:
                                    personnel.update(HolderIdCard=740054610)
                            elif k == 'InsuredName':
                                if item == '' or item == 0:
                                    personnel.update(InsuredName='壁虎科技有限公司')
                                elif '*' in item:
                                    personnel.update(InsuredName='壁虎科技有限公司')
                            elif k == 'InsuredIdType':
                                if item == '' or item == 0 or item == 1:
                                    personnel.update(InsuredIdType=2)
                            elif k == 'InsuredIdCard':
                                if item == '' or item == 0 or len(item) <= 15:
                                    personnel.update(InsuredIdCard=740054610)
                                elif '*' in item:
                                    personnel.update(InsuredIdCard=740054610)
                            else:
                                log_info_value.update(无变化关系人=personnel)
                                log.log_info(self, log_info_value)
                    if xubaovalues >= 0 and xubaovalues <= 10:
                        log_info_value.update(licenseNo=licenseNO, 续保耗时=xubaovalues)
                        log.log_info(self, current_entry=log_info_value)
                        log_info_value.update(续保结果=xubao.res, 车牌=licenseNO)
                        log.log_info(self, current_entry=log_info_value)
                        StatusMessage = xubao.res["StatusMessage"]
                        common_return_a = common_return.testxubao(self, StatusMessage)
                        returnLicenseNo = xubao.res['UserInfo']['LicenseNo']
                        returnEngineNo = xubao.res['UserInfo']['EngineNo']
                        returnModleName = xubao.res['UserInfo']['ModleName']
                        returnCarVin = xubao.res['UserInfo']['CarVin']
                        returnRegisterDate = xubao.res['UserInfo']['RegisterDate']
                        returnSource = xubao.res['SaveQuote']['Source']
                        log_info_value.update(车五项信息车牌=returnLicenseNo, 发动机=returnEngineNo, 品牌=returnModleName,
                                              车架=returnCarVin, 注册日期=returnRegisterDate, 上年投保=returnSource)
                        log.log_info(self, current_entry=log_info_value)
                        if common_return_a == True:
                            Theinsurancecompany1 = readagin.getint('Theinsurancecompany', 'insurance')
                            url1 = 'http://qa.interfaces.com/api/CarInsurance/PostPrecisePrice?'
                            data1 = {
                                'LicenseNo': xubao.res['UserInfo']['LicenseNo'],
                                'CityCode': cict1[i],
                                'Agent': Agent,
                                'ForceTax': '1',
                                'IsPublic': '0',
                                'BuJiMianCheSun': '1',
                                'BuJiMianSanZhe': '1',
                                'SiJi': '10000',
                                'ChengKe': '10000',
                                'CheSun': '1',
                                'SanZhe': '500000',
                                'CarOwnersName': personnel['LicenseOwner'],
                                'OwnerIdCardType': personnel['IdType'],
                                'IdCard': personnel['CredentislasNum'],
                                'InsuredName': personnel['PostedName'],
                                'InsuredIdType': personnel['HolderIdType'],
                                'InsuredIdCard': personnel['HolderIdCard'],
                                'HolderName': personnel['InsuredName'],
                                'HolderIdType': personnel['InsuredIdType'],
                                'HolderIdCard': personnel['InsuredIdCard'],
                                'CustKey': '4DE9B7822E0DE81FC734BC5689AB6F03',
                                'SecCode': '23c73b3be4c698971dbf320699431545',
                                'BuJiMianChengKe': '1',
                                'BuJiMianSiJi': '1',
                                'QuoteGroup': Theinsurancecompany1,
                                'SubmitGroup': '0',
                                'IsTempStorage': '1',
                            }


                            start = time.time()
                            baojia = RunMain(url1, 'GET', data1)
                            end = time.time()
                            baojavalues = int(end - start)
                            log_bug_value.update(车牌=licenseNO, 报价耗时=baojavalues)
                            log.log_bug(self, log_bug_value)
                            log_info_value.update(车牌号=licenseNO, 关系人信息车主=personnel)
                            log.log_info(self, log_info_value)
                            log_info_value.update(报价耗时=baojavalues, 报价请求=baojia.res)
                            log.log_info(self, log_info_value)
                            url2 = 'http://qa.interfaces.com/api/CarInsurance/GetPrecisePrice?'
                            data2 = {
                                'LicenseNo': xubao.res['UserInfo']['LicenseNo'],
                                'Agent': Agent,
                                'CustKey': '4DE9B7822E0DE81FC734BC5689AB6F03',
                                'SecCode': '23c73b3be4c698971dbf320699431545',
                                'TimeFormat': '1',
                                'ShowEmail': '1',
                                'QuoteGroup': Theinsurancecompany1,
                                'SubmitGroup': '0',
                                'IsTempStorage': '1',
                            }
                            baojiajg = RunMain(url2, 'GET', data2)
                            print(baojiajg.res)
                            Offer_results1 = baojiajg.res["StatusMessage"]
                            results1 = common_return.Offerresults(self, Offer_results1)
                            xianxiabaojiajieguo1['报价请求结果'] = Offer_results1
                            xianxiabaojiajieguo[licenseNO] = xianxiabaojiajieguo1.copy()
                            if results1 == True:
                                log_info_value.update(报价结果=results1)
                                QuoteResultt = baojiajg.res['Item']['QuoteResult']
                                QuoteResultt1 = baojiajg.res['Item']['QuoteStatus']
                                xianxiabaojiajieguo1['报价获取结果'] = QuoteResultt
                                xianxiabaojiajieguo[licenseNO] = xianxiabaojiajieguo1.copy()
                                Repeat_insurance = common_return.Offer_the_results(self, QuoteResultt)
                                the_same = common_return.Offer_results(self, QuoteResultt)
                                BizTotal = baojiajg.res['Item']['BizTotal']  # 商业
                                TaxTotal = baojiajg.res['Item']['TaxTotal']  # 车船
                                ForceTotal = baojiajg.res['Item']['ForceTotal']  # 交强
                                CheSun = dict_get(baojiajg.res, 'CheSun')
                                CheSunBjm = dict_get(baojiajg.res, 'BuJiMianCheSun')
                                SanZhe = dict_get(baojiajg.res, 'SanZhe')
                                SanZheBjm = dict_get(baojiajg.res, 'BuJiMianSanZhe')
                                SiJi = dict_get(baojiajg.res, 'SiJi')
                                SiJiBjm = dict_get(baojiajg.res, 'BuJiMianSiJi')
                                ChengKe = dict_get(baojiajg.res, 'ChengKe')
                                ChengKeBjm = dict_get(baojiajg.res, 'BuJiMianChengKe')
                                log_info_value.update(车牌=licenseNO, 车损=CheSun, 车损不计免赔=CheSunBjm, 三者=SanZhe,
                                                      三者不计免赔=SanZheBjm, 司机=SiJi, 司机不计免赔=SiJiBjm, 乘客=ChengKe,
                                                      乘客不计免赔=ChengKeBjm)
                                log.log_info(self, log_info_value)
                                ##QuoteStatuss报价状态，-1=未报价， 0=报价失败，>0报价成功
                                if QuoteResultt1 <= 0:
                                    log_info_value.update(报价结果=QuoteResultt)
                                    if Repeat_insurance == True:
                                        success1 = success.append(licenseNO)
                                        log_info_value.update(商业=BizTotal, 车船=TaxTotal, 交强=ForceTotal, 车牌=licenseNO,
                                                              报价结果=Repeat_insurance)
                                        log.log_info(self, log_info_value)
                                        xianxiabaojiajieguo1['商业'] = str(BizTotal)
                                        xianxiabaojiajieguo1['交强'] = str(ForceTotal)
                                        xianxiabaojiajieguo1['车船'] = str(TaxTotal)
                                        xianxiabaojiajieguo[licenseNO] = xianxiabaojiajieguo1.copy()
                                    elif the_same == True:
                                        success1 = success.append(licenseNO)
                                        log_info_value.update(商业=BizTotal, 车船=TaxTotal, 交强=ForceTotal, 车牌=licenseNO,
                                                              报价结果=the_same)
                                        log.log_info(self, log_info_value)
                                        xianxiabaojiajieguo1['商业'] = str(BizTotal)
                                        xianxiabaojiajieguo1['交强'] = str(ForceTotal)
                                        xianxiabaojiajieguo1['车船'] = str(TaxTotal)
                                        xianxiabaojiajieguo[licenseNO] = xianxiabaojiajieguo1.copy()
                                    else:
                                        defeated1 = defeated.append(licenseNO)
                                        log_info_value.update(车牌=licenseNO, 报价结果=QuoteResultt)
                                        log.log_bug(self, log_info_value)
                                        xianxiabaojiajieguo1['商业'] = str(BizTotal)
                                        xianxiabaojiajieguo1['交强'] = str(ForceTotal)
                                        xianxiabaojiajieguo1['车船'] = str(TaxTotal)
                                        xianxiabaojiajieguo[licenseNO] = xianxiabaojiajieguo1.copy()
                                else:
                                    log_info_value.update(报价结果=QuoteResultt)
                                    log_info_value.update(商业=BizTotal, 车船=TaxTotal, 交强=ForceTotal, 车牌=licenseNO,
                                                          报价结果=QuoteResultt)
                                    success1 = success.append(licenseNO)
                                    log.log_info(self, log_info_value)
                                    xianxiabaojiajieguo1['商业'] = str(BizTotal)
                                    xianxiabaojiajieguo1['交强'] = str(ForceTotal)
                                    xianxiabaojiajieguo1['车船'] = str(TaxTotal)
                                    xianxiabaojiajieguo[licenseNO] = xianxiabaojiajieguo1.copy()

                            else:
                                defeated1 = defeated.append(licenseNO)
                                xianxiabaojiajieguo1['报价请求结果'] = Offer_results1
                                xianxiabaojiajieguo[licenseNO] = xianxiabaojiajieguo1.copy()
                                log_bug_value.update(车牌=licenseNO, 异常结果=Offer_results1)
                                log.log_bug(self, log_bug_value)
                            continue

                        else:
                            defeated1 = defeated.append(licenseNO)
                            log_bug_value.update(车牌=licenseNO, 异常结果=StatusMessage)
                            log.log_bug(self, log_bug_value)
                        continue

                    else:
                        defeated1 = defeated.append(licenseNO)
                        log_bug_value.update(车牌=licenseNO, 续保耗时=xubaovalues)
                        log.log_bug(self, log_bug_value)
                        continue
                else:
                    defeated1 = defeated.append(licenseNO)
                    log_bug_value.update(车牌=licenseNO, 续保耗时=xubaovalues, 续保异常=StatusMessage)
                    log.log_bug(self, log_bug_value)
                    continue
        return xianxiabaojiajieguo