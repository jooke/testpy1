#!/usr/bin/env python
#  -*- coding:utf-8 -*-

__author__ = 'test'

import xlrd,json,os,xlwt
from xlutils.copy import copy
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from hash import hash
from interfaceTest import interface

class excel:
 def __init__(self,testCaseFile):
     self.testCaseFile=testCaseFile

 def runTest(self):

      testCaseFile = os.path.join(os.getcwd(),self.testCaseFile)
      if not os.path.exists(testCaseFile):
          logging.error('测试用例文件不存在！')
          sys.exit()
      testCase = xlrd.open_workbook(testCaseFile)


  #    sheet_name = testCase.sheet_names()[1]

  #    table = testCase.sheet_by_index(0)
      table = testCase.sheet_by_name('Sheet1')
      errorCase = []                #用于保存接口返回的内容和HTTP状态码
      s = None
      for i in range(1,table.nrows):
            #if table.cell(i, 9).value.replace('\n','').replace('\r','') != 'Yes':
             #   continue
            num = str(int(table.cell(i, 0).value)).replace('\n','').replace('\r','')
            api_purpose = table.cell(i, 1).value.replace('\n','').replace('\r','')
            api_host = table.cell(i, 2).value.replace('\n','').replace('\r','')
            request_url= table.cell(i, 3).value.replace('\n','').replace('\r','')
            request_method = table.cell(i, 4).value.replace('\n','').replace('\r','')
            request_data_type = table.cell(i, 5).value.replace('\n','').replace('\r','')
            request_data = table.cell(i, 6).value.replace('\n','').replace('\r','')
            encryption = table.cell(i, 7).value.replace('\n','').replace('\r','')
            check_point = table.cell(i, 8).value
            request_sid = table.cell(i, 10).value.replace('\n', '').replace('\r', '')
#            print  request_sid

            req = interface(num, api_purpose, api_host, request_url, request_method, request_data_type, request_data, check_point,request_sid,s)
            status, resp, s = req.interfaceTest()
            readCase = xlrd.open_workbook(testCaseFile)
            writeCase = copy(readCase)
            ws = writeCase.get_sheet(0)
            if status != 200 or check_point not in resp:            #如果状态码不为200或者返回值中没有检查点的内容，那么证明接口产生错误，保存错误信息。
                errorCase.append((num + ' ' + api_purpose, str(status), 'https://'+api_host+request_url, resp))
                ws.write(i, 11, 'fail')
            else:
                ws.write(i,11,'pass')
 #              pass

            writeCase.save(testCaseFile)



      print  "errorcase:",errorCase
      return errorCase
#test=excel('TestCase.xlsx')
#print test.runTest()


"""          if encryption == 'MD5':              #如果数据采用md5加密，便先将数据加密
                request_data = json.loads(request_data)
                h = hash(request_data['pwd'])
              request_data['pwd'] = h.md5Encode()
"""
