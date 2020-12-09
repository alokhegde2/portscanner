import socket
import termcolor  #to print statement in different colour

def scan(target,ports):
    print(f'\n Starting Sacn for {target}')
    for port in range(1,ports):
        scan_port(target,port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f"[+] Port Opened {port}")
        sock.close()

    except:
        pass

targets = input("[*] Enter Targets to scan(split them by ,): ")
ports = int(input("[*] Enter How many Ports you want to scan :"))

if ',' in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets"),'blue'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '),ports)
else:
    scan(targets,ports)


