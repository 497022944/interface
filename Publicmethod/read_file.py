import os


class Read_file:

    #读取车牌文件
    def LicenseNo_read(self):
        #读取txt车牌数据
        yongli_path = os.path.dirname(os.path.abspath('.')) + "\chepai\chepaiku.txt"
        LicenseNo_read = open(yongli_path, 'r', encoding='utf-8-sig')
        return LicenseNo_read

    #读取线上线下文件
    def Read_online_offline_files(self):
        #读取txt车牌数据
        it_path = os.path.dirname(os.path.abspath('.')) + "\chepai\itorqa.txt"
        insurancecompany_read = open(it_path, 'r', encoding='utf-8-sig')
        return insurancecompany_read

    #读取城市文件
    def Read_citi(self):
        #读取txt车牌数据
        it_path = os.path.dirname(os.path.abspath('.')) + "\chepai\citi.txt"
        Read_citi_read = open(it_path, 'r', encoding='utf-8-sig')
        return Read_citi_read