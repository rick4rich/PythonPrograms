import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host = input("[*] Enter The Host To Scan: ")

def portscanner(port):
    if sock.connect_ex((host,port)):
        print(colored("[!!]Port %d Is Closed" % (port), 'red'))

    else:
        print(colored("[+]Port %d Is Open" % (port), 'green'))

for port in range(1,1000):
    portscanner(port)
 
