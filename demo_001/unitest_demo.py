# _*_ coding:utf-8 _*-
# 作者：shangxiaoyu
# @Time : 2020/8/3 21:57
import unittest
from ddt import ddt, unpack, data
from demo_001.excel_data import ExcelData
from demo_001.operator_common import OperatorCommon
import jsonpath
import json

@ddt
class UnitestDemo(unittest.TestCase):

    #读取测试用例中的数据
    dataList =  ExcelData().getExcel()

    @classmethod
    def setUpClass(cls) -> None:
        #定义一个类变量，存储接口依赖数据
        cls.varDict = {}
        #执行测试用例前只加载一次测试用例数据
        # cls.dataList = ExcelData().getExcel()

    @classmethod
    def tearDownClass(cls) -> None:
        print(cls.varDict)

    @data(*dataList)
    @unpack
    def test_excel(self, url, body, header, method, method_type, expect, dependency):
        #实例化共同类对象
        common = OperatorCommon()
        #数据转换
        body = common.convertData(self.varDict, body)
        header = common.convertData(self.varDict, header)
        #接口请求
        res = common.request(url, body, header, method, method_type)
        #依赖变量名不是"/"，存储到字典中
        if len(dependency)> 0 and dependency.find("/") < 0 :
            self.varDict[dependency] = res.json()
        print("接口返回值：", res.json())
        #期望值转换成json对象
        expect = json.loads(expect)
        print("预期值：" , expect)
        flg = True
        for (k, v)  in expect.items():
            # 断言：实际值
            reality = jsonpath.jsonpath(res.json(), k)[0]
            # 如果实际值等于期望值
            if reality != v:
                flg = False
                break
        #断言
        self.assertTrue(flg, msg="响应失败")