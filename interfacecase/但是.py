import re
import time
import datetime


name = [1,2,3,4]
lins = ['ss','sdd','ff','fff','hh']

v = len(name)*100/len(lins)
v1 = round(v)
print("结果是：{}%".format(v1))

linss = ['京J9789o', '苏j9789o', '粤j9789o']
#linss = ['京J9789o苏j9789o粤j9789o']
for i in linss:
    # #str1 = ''.join(str(x) for x in i)
    # ree = i[:2:1]
    # reee = re.findall('\w京{1,2}',ree , re.S)

    #REE = re.findall('\w[A-Za-z]{1}', i, re.S)
    n = i.upper()
    s = re.findall('^([京津沪渝冀豫云辽黑湘皖鲁新苏浙赣鄂桂甘晋蒙陕吉闽贵粤青藏川宁琼使领台]{1}[A-Z]{1})', n, re.S)
    print(s)
tim = ['2016-04-07 10:25:09']
k = ','.join(str(ti) for ti in tim)
j = k[:10:1]
ti = time.strftime("%Y-%m-%d", time.localtime())
print(ti,j)
d1 = datetime.datetime.strptime(j, '%Y-%m-%d')
d2 = datetime.datetime.strptime(ti, '%Y-%m-%d')
delta = d1 - d2
print(delta.days)


ht = {
    "BusinessStatus": 1,
    "CustKey": "4DE9B7822E0DE81FC734BC5689AB6F03",
    "Item": {
        "BizRate": 0,
        "BizTotal": 3255.97,
        "BoLi": {
            "BaoE": 0,
            "BaoFei": 0
        },
        "BuJiMianCheSun": {
            "BaoE": 1,
            "BaoFei": 332.22
        },
        "BuJiMianChengKe": {
            "BaoE": 1,
            "BaoFei": 5.97
        },
        "BuJiMianDaoQiang": {
            "BaoE": 0,
            "BaoFei": 0
        },
        "BuJiMianHuaHen": {
            "BaoE": 0,
            "BaoFei": 0
        },
        "BuJiMianJingShenSunShi": {
            "BaoE": 0,
            "BaoFei": 0
        },
        "BuJiMianSanZhe": {
            "BaoE": 1,
            "BaoFei": 84.46
        },
        "BuJiMianSheShui": {
            "BaoE": 0,
            "BaoFei": 0
        },
        "BuJiMianSiJi": {
            "BaoE": 0,
            "BaoFei": 0
        },
        "BuJiMianZiRan": {
            "BaoE": 0,
            "BaoFei": 0
        },
        "CheSun": {
            "BaoE": 314384,
            "BaoFei": 2214.82
        },
        "ChengKe": {
            "BaoE": 10000,
            "BaoFei": 39.78
        },
        "DaoQiang": {
            "BaoE": 0,
            "BaoFei": 0
        },
        "ForceRate": 0,
        "ForceTotal": 798.35,
        "HcHuoWuZeRen": {
            "BaoE": 0,
            "BaoFei": 0
        },
        "HcJingShenSunShi": {
            "BaoE": 0,
            "BaoFei": 0
        },
        "HcSanFangTeYue": {
            "BaoE": 0,
            "BaoFei": 0
        },
        "HcSheBeiSunshi": {
            "BaoE": 0,
            "BaoFei": 0
        },
        "HcXiuLiChang": {
            "BaoE": 0,
            "BaoFei": 0
        },
        "HuaHen": {
            "BaoE": 0,
            "BaoFei": 0
        },
        "QuoteResult": "报价成功",
        "QuoteStatus": 1,
        "RateFactor1": 0.6,
        "RateFactor2": 0.75,
        "RateFactor3": 0.85,
        "RateFactor4": 1.0,
        "SanZhe": {
            "BaoE": 500000,
            "BaoFei": 563.04
        },
        "SheShui": {
            "BaoE": 0,
            "BaoFei": 0
        },
        "SiJi": {
            "BaoE": 10000,
            "BaoFei": 15.68
        },
        "Source": 8,
        "TaxTotal": 400,
        "ZiRan": {
            "BaoE": 0,
            "BaoFei": 0
        }
    },
    "StatusMessage": "获取报价信息成功",
    "UserInfo": {
        "BusinessExpireDate": "2019-09-28 23:59:59",
        "BusinessStartDate": "2019-09-29 00:00:00",
        "Email": "",
        "ForceExpireDate": "2019-09-28 23:59:59",
        "ForceStartDate": "2019-09-29 00:00:00",
        "HolderIdCard": "412828198503066314",
        "HolderIdType": 1,
        "HolderMobile": "13503371701",
        "HolderName": "北京同德兴商贸中心",
        "InsuredIdCard": "412828198503066314",
        "InsuredIdType": 1,
        "InsuredMobile": "13503371701",
        "InsuredName": "北京同德兴商贸中心",
        "LicenseNo": "京Q9J1Y5"
    }
}
def dict_get(dict1, objkey, default=None):
        for k, v in dict1.items():
            if k == objkey:
                return v
            else:
                if type(v) is dict:
                    ret = dict_get(v, objkey)
                    if ret is not default:
                        return ret

a = dict_get(ht, 'BizTotal')
print(a)

