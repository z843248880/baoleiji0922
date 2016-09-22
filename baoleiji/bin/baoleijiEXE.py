#!/usr/bin/env python

import os
import sys
import json
import threading
import paramiko

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)

from ssh_cmd import ssh_cmd
from ssh_sftp import ssh_sftp

with open(BASEDIR + '/conf/' + 'user_info') as f:
    user_info = json.loads(f.read())

with open(BASEDIR + '/conf/' + 'server_info') as fs:
    server_info = json.loads(fs.read())

def printOneList():
    for num in range(1,len(server_info)+1):
        son_dict = server_info[str(num)]
        for key in son_dict:
            print('%s. %s' % (num,key))
            print(son_dict[key],end = ' ')
        print('\n')


print('please select:')
printOneList()
dict_one = {
    '1':'xitong',
    '2':'kaifa',
    '3':'ceshi'
    }
thread_list = []
user_choice = input('enter a number(enter q to exit.):')
while user_choice != 'q':
    if server_info.get(user_choice):
        server_list = server_info[user_choice][dict_one[user_choice]]
        username_choice = input('root/sa:')
        cmd_user_input = input('cmd:')
        if cmd_user_input.startswith('get') or cmd_user_input.startswith('put'):
            while True:
                source_input_file = input('enter source file:')
                if not source_input_file:continue
                destination_input_file = input('enter destination file:')
                if not destination_input_file:continue
                break
        for ip in server_list:
            if user_info.get(ip):
                port = int(user_info[ip][0])
                try:
                    passwd = user_info[ip][1][username_choice]
                except KeyError as e:
                    print('error:{} is not exist.'.format(e))
                    continue
                if cmd_user_input.startswith('get') or cmd_user_input.startswith('put'):
#                     t = ssh_sftp(ip,port,username_choice,passwd,cmd_user_input,source_input_file,destination_input_file)
                    t = threading.Thread(target=ssh_sftp,args=(ip,port,username_choice,passwd,cmd_user_input,source_input_file,destination_input_file))
                    thread_list.append(t)
                    t.start()
                else:
#                     t = ssh_cmd(ip,port,username_choice,passwd,cmd_user_input)
                    t = threading.Thread(target=ssh_cmd,args=(ip,port,username_choice,passwd,cmd_user_input))
                    thread_list.append(t)
                    t.start()
        for i in thread_list:
            i.join()
    user_choice = input('enter a number(enter q to exit.):')





