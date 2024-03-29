import configparser
import os

class read_ini:
    def Read_ini_loading(self):
        root_dir = os.path.dirname(os.path.abspath('.'))  # 获取当前文件所在目录的上一级目录，即项目所在目录E:\Crawler
        cf = configparser.ConfigParser()
        cf.read(root_dir+"/Config/conf.ini", encoding='utf-8-sig')  # 拼接得到config.ini文件的路径，直接使用
        return cf
        # secs = cf.sections()  # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置，每个section由[]包裹，即[section])，并以列表的形式返回
        # print(secs)
        # options = cf.options("M")  # 获取某个section名为Mysql-Database所对应的键
        # print(options)
        # items = cf.items("M")  # 获取section名为Mysql-Database所对应的全部键值对
        # print(items)
        # host = cf.get("M", "host")  # 获取[Mysql-Database]中host对应的值
        # print(host)