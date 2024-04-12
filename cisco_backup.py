import paramiko, time, getpass
from datatime import datetime

def auto_cisco_backup(ip, port, user, passwd, enablepasswd):
    print('backup start')
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip=ip, port=port, username=user, password=passed)
    
    with open("backup_cmd.csv", 'r', encoding='utf-8') as f:
        cmds = f.read().split('\n')
        
    chan = client.invoke_shell()
    time.sleep(.5)
    chan.send('en\n')
    chan.send(enablepasswd+'\n')
    time.sleep(.5)
    for cmd in cmds:
        chan.send(cmd+'\n')
        time.sleep(1)
        
    outputs = chan.recv(99999)
    with open(f"{ip}_{datetime.now().strftime('%Y%m%d')}.txt", 'a+') as f:
        f.write(str(outputs.decode('utf-8')))
    
    print('backup success')
    client.close()
    return
    
ip = input('ip = ')
user = input('user = ')
passwd = getpass.getpass('passwd = ')
enablepasswd = getpass.getpass('enablepasswd = ')

auto_cisco_backup(ip=ip, port=22, user=user, passwd=passwd, enablepasswd=enablepasswd)