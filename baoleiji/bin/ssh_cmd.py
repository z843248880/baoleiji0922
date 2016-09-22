#!/usr/bin/env python

import os
import sys
import paramiko
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
def ssh_cmd(recv_ip,recv_port,recv_username,recv_password,recv_cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=recv_ip, port=recv_port, username=recv_username, password=recv_password)
    stdin, stdout, stderr = ssh.exec_command(recv_cmd)
    res = stdout.read()
    err = stderr.read()
    result = res if res else err
    print('-------{}-------'.format(recv_ip))
    print(result.decode())
#     return (result.decode())
    ssh.close() 