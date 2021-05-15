#!/usr/bin/python3

import socket,sys,lista,os
from datetime import datetime

if len(sys.argv) != 2:
	print("=-----------------------------------------------------=")
	print("|           PortScan v1 - Coded By Vida               |")
	print("|Modo de Uso: portscan.py 192.168.0.1 \ ou example.com|")
	print("=-----------------------------------------------------=")
else:
	def portscan(ip):
		print("\t\t[+]","PortScan ->",ip," [+]")
		conf = bool(os.system("ping -c1 {} 2>/dev/null 1>/dev/null".format(ip)))
		if(conf == False):
			ports = lista.getlista()
			print("[>] Portas Scaneadas:")
			print(ports,"\n")
			for alvo in ports:
				psocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				socket.setdefaulttimeout(0.5)
				if(psocket.connect_ex((ip,alvo)) == 0):
					print("\t==========Resultado=========")
					print("\t[+] Porta Aberta -> ",alvo)
					psocket.close()
				else:
					psocket.close()
			print("\t---=Scaneamento Completo=---")
		else:
			print("[-] Host Indisponivel [-]")
	inicio = datetime.now()
	try:
		portscan(sys.argv[1])
	except:
		exit()
	fim = datetime.now()
	print("\nScan Durou -> ",(fim-inicio))
