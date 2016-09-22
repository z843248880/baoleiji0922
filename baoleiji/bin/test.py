import paramiko
 
transport = paramiko.Transport(('10.103.16.72',9880))
transport.connect(username='sa',password='123456')
 
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
# sftp.put('/tmp/location.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
sftp.get('/home/sa/passwd', '/home/sa/passwd1')
 
transport.close()