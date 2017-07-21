#!/usr/bin/env python
#  -*- coding:utf-8 -*-
from TestCase.conf import confs
import smtplib
from email.mime.text import MIMEText
class mail:
  def __init__(self,text):
      self.text=text

  def sendMail(self):
      cf=confs()
      mail_info = cf.get_conf()
      sender = mail_info['sender']
      receiver = mail_info['receiver']
      subject = '[AutomationTest]接口自动化测试报告通知'
      smtpserver = mail_info['smtpserver']
      username = mail_info['username']
      password = mail_info['password']
      msg = MIMEText(self.text,'html','utf-8')
      msg['Subject'] = subject
      msg['From'] = sender
      msg['To'] = ''.join(receiver)
      smtp = smtplib.SMTP()
      smtp.connect(smtpserver)
      smtp.login(username, password)
      smtp.sendmail(sender, receiver, msg.as_string())
  #    print "www"
 #     print smtp
      smtp.quit()
