#!/usr/bin/env python

import os,sys,json
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

user_info_dict = {
    '192.168.0.30':['22',{'root':'xi','sa':'123456'}],
    '10.103.16.67':['9880',{'sa':'123456'}],
    '10.103.16.72':['9880',{'sa':'123456'}]
    }

with open(BASEDIR + '/conf/' + 'user_info','w') as f:
    f.write(json.dumps(user_info_dict))


