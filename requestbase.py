#!/usr/bin/env python
#  -*- coding:utf-8 -*-
# encoding=utf8

import requests
def insert():

 headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, compress',
           'Accept-Language': 'en-us;q=0.5,en;q=0.3',
           'Cache-Control': 'max-age=0',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
 cookies = {'sid':'85a63b8c-bb6b-40f4-b64e-564e28cd0bec'}
 jsons = '{"merge_task":{"merge_task_name":"dbtest1","task_group_id":"0","merge_task_priority":1,"task_way":"1","time_plan":"00:00:00","is_send_result":0,"is_ftp_upload":0,"send_mail":"","report_type":"1","report_module":"-3"},"crack_params":[{"crack_flag":0,"crack_type":"mysql","crack_user_id":17,"crack_pwd_id":18},{"crack_flag":0,"crack_type":"oracle","crack_user_id":19,"crack_pwd_id":20},{"crack_flag":0,"crack_type":"db2","crack_user_id":21,"crack_pwd_id":22},{"crack_flag":0,"crack_type":"sqlserver","crack_user_id":23,"crack_pwd_id":24},{"crack_flag":0,"crack_type":"sybase","crack_user_id":25,"crack_pwd_id":26},{"crack_flag":0,"crack_type":"informix","crack_user_id":27,"crack_pwd_id":28},{"crack_flag":0,"crack_type":"dm","crack_user_id":29,"crack_pwd_id":30}],"scan_param":{"scan_thread_num":"60","report_paranoia":"2","tcp_scan_type":0,"task_id":"0","online_scan_type":"1","online_scan_port":"80,443,139,445,3389,22,23,1433,1521,1533,3306,5000,5236,50000","debug_flag":0,"max_scan_host_num":30,"param_model_id":1,"vul_scan_time":"120","max_scan_thread_num":100,"udp_port_time":"1","is_refuse_concur":1,"scan_risk":"c,h,m,l,i,","crack_count":"250","tcp_port_time":"300","is_rely_scan":1,"scan_param_id":1,"tcp_port_scope":"1433,1521,1533,3306,5000,5236,50000","scan_host_num":"15","is_safe_scan":1,"online_timeout":"4","is_force_scan":0,"udp_port_scope":"none","udp_scope_type":"4","tcp_scope_type":"3"},"task_targets":[{"scan_target":"192.168.162.132","nvs_policy_id":"2"}],"target_ward_params":[{"scan_target":"192.168.162.132","ward_params":[{"jump_ip":"用户名","param_type":0,"param_name":"MySQL","param_key":"User","param_value":"root","param_belong":0},{"jump_ip":"密码","param_type":0,"param_name":"MySQL","param_key":"Pass","param_value":"test-123","param_belong":0},{"jump_ip":"端口","param_type":0,"param_name":"MySQL","param_key":"Port","param_value":"3306","param_belong":0},{"jump_ip":"数据库名","param_type":0,"param_name":"MySQL","param_key":"DbName","param_value":"","param_belong":0},{"jump_ip":"配置路径","param_type":0,"param_name":"MySQL","param_key":"ConfPath","param_value":"","param_belong":0},{"jump_ip":"用户名","param_type":0,"param_name":"SQLServer","param_key":"User","param_value":"sa","param_belong":0},{"jump_ip":"密码","param_type":0,"param_name":"SQLServer","param_key":"Pass","param_value":"test-123","param_belong":0},{"jump_ip":"端口","param_type":0,"param_name":"SQLServer","param_key":"Port","param_value":"1433","param_belong":0},{"jump_ip":"数据库名","param_type":0,"param_name":"SQLServer","param_key":"DbName","param_value":"","param_belong":0},{"jump_ip":"配置路径","param_type":0,"param_name":"SQLServer","param_key":"ConfPath","param_value":"","param_belong":0}]}]}'
 data= {'task_json': jsons, 'module_type': 'db'}
 _URL = 'https://192.168.162.94/ndasec/task/insertTask.do'
 response=requests.post(_URL,data=data,headers=headers,cookies=cookies,verify=False)
 print response.status_code
 print response.text

if __name__ == "__main__":
    insert()
