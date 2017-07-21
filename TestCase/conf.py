#!/usr/bin/env python
#  -*- coding:utf-8 -*-
__author__ = 'test'

import ConfigParser
import os
class confs:

  def __init__(self):
     pass
  def get_conf(self):
    conf_file = ConfigParser.ConfigParser()

    conf_file.read(os.path.join(os.getcwd(),'conf.ini'))


    conf = {}

    conf['sender'] = conf_file.get("email","sender")

    conf['receiver'] = conf_file.get("email","receiver")

    conf['smtpserver'] = conf_file.get("email","smtpserver")

    conf['username'] = conf_file.get("email","username")

    conf['password'] = conf_file.get("email","password")

    return conf


"""
test=confs()
mail_info = test.get_conf()
print mail_info
sender = mail_info['sender']
receiver = mail_info['receiver']
subject = '[AutomationTest]接口自动化测试报告通知'
smtpserver = mail_info['smtpserver']
username = mail_info['username']
password = mail_info['password']
print sender,receiver,subject,smtpserver,username,password
"""

#  print "当前工作目录 : %s" % os.getcwd()