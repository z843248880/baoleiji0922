#!/usr/bin/env python


import paramiko
import uuid

res = 'zxc'
err = ''
result = res if res else err
if result == '':
    print('123')
else:
    print(result)













# ssh = paramiko.SSHClient()
# # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='192.168.0.55', port=22, username='root', password='xi')
# stdin, stdout, stderr = ssh.exec_command('df -hl')
# result = stdout.read()
# print(result.decode())
# ssh.close()