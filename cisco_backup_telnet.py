import telnetlib, time, getpass
from datetime import datetime

def telnet_command(ip, passwd, enablepasswd):
    print('start backup')

    with open("backup_cmd.csv", 'r', encoding='utf-8') as f:
        cmds = f.read().split('\n')
        
    tn = telnetlib.Telnet(ip)
    tn.read_until(b'Password:')
    tn.write(passwd.encode('ascii') + b'\n')
    tn.write(b'en\n')
    tn.write(enablepasswd.encode('ascii') + b'\n')
    for cmd in cmds:
        tn.write(cmd.encode('ascii') + b'\n')
        
    with open(f"{ip}_{datetime.now().strftime('%Y%m%d')}.txt", 'a+') as f:
        f.write(tn.read_until(b'FIN\n', timeout = 3).decode('ascii'))
    tn.close()
    print('backup sucess')
    return
    
ip = input('ip = ')
passwd = getpass.getpass('passwd = ')
enablepasswd = getpass.getpass('enablepasswd = ')

telnet_command(ip=ip, passwd=passwd, enablepasswd=enablepasswd)