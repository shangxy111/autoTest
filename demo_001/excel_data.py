# _*_ coding:utf-8 _*-
# 作者：shangxiaoyu
# @Time : 2020/8/2 21:23
import openpyxl
import os

class ExcelData:
    def getExcel(self):
        print("读取测试用例")
        root_dir = os.path.dirname(os.path.abspath(__file__))
        #读取case.xlsx文件
        wb = openpyxl.load_workbook(os.path.join(root_dir, 'case1.xlsx'))
        #获取sheet页
        sheet = wb['Sheet2']
        #获取行元素
        row_sheet = sheet.iter_rows()
        #定义一个变量用来存储测试用例行数据
        rows_List = []
        #遍历每一行
        for row in row_sheet:
            #表头一行不作处理
            if row[0].value == 'url' :
                continue
            # 行元素
            item = []
            #读取每行中单元格中数据
            for col in row:
                item.append(col.value)
            #将行元素的值存放在list中
            rows_List.append(item)
        return rows_List

if __name__ == '__main__':
    # ExcelData().getExcel()
    pass
