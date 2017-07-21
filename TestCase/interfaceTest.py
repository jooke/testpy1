# !/usr/bin/env python
#  -*- coding:utf-8 -*-
# encoding=utf8
__author__ = 'test'

import requests
import sys
import re
import json
reload(sys)
sys.setdefaultencoding('utf8')

from log.log import logs
class interface:
    def __init__(self,num, api_purpose, api_host,request_url, request_method,request_data_type, request_data, check_point,request_sid,s=None):
        self.num=num
        self.api_purpose=api_purpose
        self.request_url=request_url
        self.api_host=api_host
        self.request_method=request_method
        self.request_data_type=request_data_type
        self.request_data=request_data
        self.check_point=check_point
        self.s=s
        self.request_sid=request_sid
    def interfaceTest(self):
        headers = {'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest'}
    # cookies = {'sid': 'ff877b98-f25f-4ec3-9b73-4a3d3abe780a'}
        cookies=eval(self.request_sid)

    #     jsons = '{"merge_task":{"merge_task_name":"dbtest1","task_group_id":"0","merge_task_priority":1,"task_way":"1","time_plan":"00:00:00","is_send_result":0,"is_ftp_upload":0,"send_mail":"","report_type":"1","report_module":"-3"},"crack_params":[{"crack_flag":0,"crack_type":"mysql","crack_user_id":17,"crack_pwd_id":18},{"crack_flag":0,"crack_type":"oracle","crack_user_id":19,"crack_pwd_id":20},{"crack_flag":0,"crack_type":"db2","crack_user_id":21,"crack_pwd_id":22},{"crack_flag":0,"crack_type":"sqlserver","crack_user_id":23,"crack_pwd_id":24},{"crack_flag":0,"crack_type":"sybase","crack_user_id":25,"crack_pwd_id":26},{"crack_flag":0,"crack_type":"informix","crack_user_id":27,"crack_pwd_id":28},{"crack_flag":0,"crack_type":"dm","crack_user_id":29,"crack_pwd_id":30}],"scan_param":{"scan_thread_num":"60","report_paranoia":"2","tcp_scan_type":0,"task_id":"0","online_scan_type":"1","online_scan_port":"80,443,139,445,3389,22,23,1433,1521,1533,3306,5000,5236,50000","debug_flag":0,"max_scan_host_num":30,"param_model_id":1,"vul_scan_time":"120","max_scan_thread_num":100,"udp_port_time":"1","is_refuse_concur":1,"scan_risk":"c,h,m,l,i,","crack_count":"250","tcp_port_time":"300","is_rely_scan":1,"scan_param_id":1,"tcp_port_scope":"1433,1521,1533,3306,5000,5236,50000","scan_host_num":"15","is_safe_scan":1,"online_timeout":"4","is_force_scan":0,"udp_port_scope":"none","udp_scope_type":"4","tcp_scope_type":"3"},"task_targets":[{"scan_target":"192.168.162.132","nvs_policy_id":"2"}],"target_ward_params":[{"scan_target":"192.168.162.132","ward_params":[{"jump_ip":"用户名","param_type":0,"param_name":"MySQL","param_key":"User","param_value":"root","param_belong":0},{"jump_ip":"密码","param_type":0,"param_name":"MySQL","param_key":"Pass","param_value":"test-123","param_belong":0},{"jump_ip":"端口","param_type":0,"param_name":"MySQL","param_key":"Port","param_value":"3306","param_belong":0},{"jump_ip":"数据库名","param_type":0,"param_name":"MySQL","param_key":"DbName","param_value":"","param_belong":0},{"jump_ip":"配置路径","param_type":0,"param_name":"MySQL","param_key":"ConfPath","param_value":"","param_belong":0},{"jump_ip":"用户名","param_type":0,"param_name":"SQLServer","param_key":"User","param_value":"sa","param_belong":0},{"jump_ip":"密码","param_type":0,"param_name":"SQLServer","param_key":"Pass","param_value":"test-123","param_belong":0},{"jump_ip":"端口","param_type":0,"param_name":"SQLServer","param_key":"Port","param_value":"1433","param_belong":0},{"jump_ip":"数据库名","param_type":0,"param_name":"SQLServer","param_key":"DbName","param_value":"","param_belong":0},{"jump_ip":"配置路径","param_type":0,"param_name":"SQLServer","param_key":"ConfPath","param_value":"","param_belong":0}]}]}'
    #     data = {'task_json': jsons, 'module_type': 'db'}
    #    print type(self.request_data)
        data=eval(self.request_data)



    #   if self.s == None:
    #     self.s = requests.session()
    #   if self.request_method == 'POST':
    #        if self.request_url != '/login' :

        self.s = requests.session()
        r = self.s.post(url=self.api_host+self.request_url, data = data, headers = headers,cookies=cookies,verify=False)         #由于此处数据没有经过加密，所以需要把Json格式字符串解码转换成**Python对象**
    #    r = requests.post(url=self.api_host + self.request_url, data=data, headers=headers, cookies=cookies, verify=False)
    #        elif self.request_url == '/login' :
    #          self.s = requests.session()
    #          r = self.s.post(url=self.api_host+self.request_url, data = self.request_data, headers = headers)          #由于登录密码不能明文传输，采用MD5加密，在之前的代码中已经进行过json.loads()转换，所以此处不需要解码
    #  else:
    #        logging.error(self.num + ' ' + self.api_purpose + '  HTTP请求方法错误，请确认[Request Method]字段是否正确！！！')
    #       self.s = None
    #       return 400, resp, self.s
        status = r.status_code
        resp = r.text
        print resp
    #     return status, resp, self.s
        logging=logs()
        ck=str(self.check_point)
        if status == 200 :
            if re.search(ck, str(r.text)):
                logging.logging.info(self.num + ' ' + self.api_purpose + ' 成功，' + str(status) + ', ' + str(r.text))
                return status, resp, self.s
            else:
                logging.logging.error(self.num + ' ' + self.api_purpose + ' 失败！！！，[' + str(status) + '], ' + str(r.text))
                return 200, resp , None
        else:
            logging.logging.error(self.num + ' ' + self.api_purpose + '  失败！！！，[' + str(status) + '],' + str(r.text))
            return status, resp.decode('utf-8'), None

