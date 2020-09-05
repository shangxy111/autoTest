# _*_ coding:utf-8 _*-
# 作者：shangxiaoyu
# @Time : 2020/8/10 21:49
from  HTMLTestRunner import HTMLTestRunner
import time
import unittest
import os

class Report:
    def to_report(self):
        #获取系统当前时间
        # now = time.strftime('%Y%m%d%H%M%S', time.localtime())
        #报告存储路径
        file_name = 'report.html'
        #报告存放目录
        root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report")
        #报告路径
        file_path = os.path.join(root_dir, file_name)
        # 如果存在，先清空旧报告
        if  os.path.exists(file_path):
            os.remove(file_path)
            # 如果目录不存在
        elif os.path.exists(root_dir) is False:
            os.mkdir(root_dir)
        print(root_dir, file_path)
        #生成新报告文件
        with open(file_path, "wb") as file:
            # 生成HTML报告
            runner = HTMLTestRunner(stream=file, verbosity=2, title='接口测试自动化报告', description='接口测试报告')
            #创建测试套件
            test_suit = unittest.defaultTestLoader.discover("",pattern='unitest_demo.py')
            #运行测试套件
            runner.run(test_suit)
        #发送邮件
        # Mail().send_mail(fileName)

if __name__ == '__main__':
    # 生成测试报告
    Report().to_report()
