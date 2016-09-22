#!/usr/bin/env python

import paramiko

transport = paramiko.Transport(('192.168.0.55',22))
transport.connect(username='root',password='xi')

sftp = paramiko.SFTP.from_transport(transport)
sftp.put('test.py','/tmp/test.testSftp.py')
sftp.get('/etc/passwd','/root/workspace/day09/practice/passwd.testSftp.py')

transport.close()
