#!/usr/bin/env python
#  -*- coding:utf-8 -*-
__author__ = 'test'
from TestCase.excel import excel
from TestCase.mail import mail

def main():
      testcase=excel('TestCase/TestCase.xls')
      errorTest = testcase.runTest()


      if len(errorTest) > 0:
                html = '<html><body>接口自动化扫描，共有 ' + str(len(errorTest)) + ' 个异常接口，列表如下：' + '</p><table><tr><th style="width:100px;text-align:left">接口</th><th style="width:50px;text-align:left">状态</th><th style="width:200px;text-align:left">接口地址</th><th   style="text-align:left">接口返回值</th></tr>'
                for test in errorTest:
                    html = html + '<tr><td style="text-align:left">' + test[0] + '</td><td style="text-align:left">' + test[1] + '</td><td style="text-align:left">' + test[2] + '</td><td style="text-align:left">' + test[3] + '</td></tr>'
                    mails = mail(html)
                    print html
                    mails.sendMail()

      mails=mail('ok')
      mails.sendMail()

if __name__ == '__main__':
    main()





