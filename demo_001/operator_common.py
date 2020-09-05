# _*_ coding:utf-8 _*-
# 作者：shangxiaoyu
# @Time : 2020/8/3 22:01
import requests
import json
import jsonpath

class OperatorCommon:

    #转换参数中变量
    def convertData(self, jsonObj, strObj):
        if strObj is None or jsonObj is None:
            return None
        else:
            #对字符串进行切片
            listStr =  strObj.split("$")
            #遍历字符串，取下标为奇数位的元素
            for index in range(len(listStr)):
                if index % 2 == 1:
                    #变量
                    var = listStr[index]
                    #依赖值
                    dependKey = var[0:var.find(".")]
                    #关联依赖中的变量
                    dependValue = var[var.find(".")+1:]
                    #替换依赖关系中的变量
                    vars = jsonpath.jsonpath(jsonObj[dependKey], "$."+dependValue)[0]
                    listStr[index] = str(vars)
            #返回list对象
            return "".join(listStr)

    #接口请求共同方法
    def request(self, url, data, header, method, methodType):
        #接口的请求方式：post
        if method.lower() == "post":
            #以json串的形式提交数据
            if methodType == 'json':
                #将json对象转换成字符串
                body = json.dumps(eval(data))
                #header字符串转换成源对象
                header = eval(header)
                return requests.post(url, headers=header, data=body)
            #以表单的形式提交
            elif methodType == "from":
                print("post:", url, header, data)
                return requests.post(url, headers=header, data=data)

        #接口的请求方式：get
        elif method.lower() == "get":
            #URL后面拼接参数的形式提交数据
            if methodType == 'url':
                #参数拼接在URL中
                if data is not None:
                    url = "%s?%s"%(url , data)
                if header is not None :
                    # 将json字符串转换成对象
                    header = json.loads(header)
                #返回get请求的响应结果
                return requests.get(url=url, headers=header)
            #以params形式提交数据
            else:
                #返回响应结果
                return requests.get(url=url, params=data, headers=header)




if __name__ == '__main__':
    jsonObj ={"cartinfo":{"data":[{"cartid": 8888}]},
              "uservar":{"data":[{"openid": "XDVCCC", "userid": "adbcddd123456"}]} ,
              "productvar":{"data":[{"productid": 187524233}]},
              "loginvar" : {"token":"1234566666"}
    }


