#!/usr/bin/env python

import os,sys,json
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)


server_info_dict = {
        '1':{'xitong':['192.168.0.30','10.103.16.67','10.103.16.72']},
        '2':{'kaifa':['10.103.16.67','192.168.0.30','10.103.16.72']},
        '3':{'ceshi':['10.103.16.72','192.168.0.30','10.103.16.67']}
    }


# server_info_dict = {
#     '1':{
#         'xitong':{
#             '10.103.16.67':['root','sa'],'10.103.16.72':['root','sa']}
#          },
#     '2':{
#         'kaifa':{
#             '10.103.16.67':['root','sa'],'10.103.16.72':['root','sa']}
#          },
#     '3':{
#         'ceshi':{
#             '10.103.16.67':['root','sa'],'10.103.16.72':['root','sa']}
#          }
#     }

with open(BASEDIR + '/conf/' + 'server_info', 'w') as f:
    f.write(json.dumps(server_info_dict))
    

