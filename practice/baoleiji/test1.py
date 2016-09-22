#!/usr/bin/env python

dic = {
    'alex': [
        '172.16.103.189',
        'c10.puppet.com',
        'c11.puppet.com',
    ],
    'eric': [
        'c100.puppet.com',
    ]
}
 
host_list = dic['alex']
 
print('please select:')
for index, item in enumerate(host_list, 3):
    print(index, item)
 
inp = input('your select (No):')
inp = int(inp)
hostname = host_list[inp-1]
port = 22
