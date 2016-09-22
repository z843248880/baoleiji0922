import paramiko

def ssh_sftp(recv_ip,recv_port,recv_username,recv_password,recv_cmd,source_file,destination_file): 
    transport = paramiko.Transport((recv_ip,recv_port))
    transport.connect(username=recv_username,password=recv_password)
     
    sftp = paramiko.SFTPClient.from_transport(transport)
    if recv_cmd == 'get':
        print('-------{}-------'.format(recv_ip))
        get(source_file,destination_file,sftp)       
    elif recv_cmd == 'put':
        print('-------{}-------'.format(recv_ip))
        put(source_file, destination_file,sftp)        
    transport.close()
def get(source_file,destination_file,sftp):
    sftp.get(source_file, destination_file)    
    print('get ok.')
def put(source_file,destination_file,sftp):
    sftp.put(source_file, destination_file)
    print('put ok.')
# ssh_sftp('192.168.0.30', 22, 'root', 'xi', 'put', '/etc/passwd', '/tmp/passwd')