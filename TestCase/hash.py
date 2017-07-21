#!/usr/bin/env python
#  -*- coding:utf-8 -*-
import hashlib
class hash:
  def __init__(self,data):
      self.data=data
  def md5Encode(slef):
      hashobj = hashlib.md5()
      hashobj.update(data.encode('utf-8'))
      return hashobj.hexdigest()