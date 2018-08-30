#!/usr/bin/evn python
#encoding=utf-8
#Author:canxue


import paramiko
# 创建SSH对象
#AttributeError: module 'paramiko' has no attribute 'SSHConfig'→才说了文件名不能随便整，你弄个paramiko你几个意思啊
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.129.147', port=22, username='root', password='yl631092')
# 执行命令，别整个一直输出的命令，如'ping www.baidu.com'
stdin, stdout, stderr = ssh.exec_command('df -h')
# 获取命令结果
#IOError: File is not open for reading
var_in = stdin
var_out = stdout.read()
var_err = stderr.read()
print 'var_in:',var_in,'\n','var_out:',var_out,'\n','var_err:',var_err
# 关闭连接
ssh.close()

transport = paramiko.Transport(('192.168.129.147', 22))
transport.connect(username='root', password='yl631092')
sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('G:\python\\addr_dic.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path，针对的是文件
#IOError: [Errno 13] Permission denied: 'G:\\python'
#sftp.get('/root/py_histfile', 'G:\python')
#sftp.get('/root/py_histfile', 'G:\\python\\new_name')
sftp.get('/root/py_histfile', 'new_name')
transport.close()
