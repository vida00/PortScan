#!/usr/bin/python3

def getlista():
        lista_top10 = [21,22,23,25,80,110,139,443,445,3389]
        lista_top20 = [135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
        lista_top30 = [3389,5060,5666,5900,6001,8000,8008,8080,8443,8888,10000,32768,49152,49154]
        lista_all = (lista_top10+lista_top20+lista_top30)
        all_ports = range(1,65535)
        print("1 -> TOP 10")
        print("2 -> TOP 20")
        print("3 -> TOP 30")
        print("4 -> ALL Lists")
        print("5 -> ALL Ports")
        try:
        	resp = int(input("Escolha: "))

        	lista_escolhida = []

        	if(resp == 1):
                	lista_escolhida = lista_top10
                	return lista_escolhida
        	elif(resp == 2):
                	lista_escolhida = lista_top20
                	return lista_escolhida
        	elif(resp == 3):
                	lista_escolhida = lista_top30
                	return lista_escolhida
        	elif(resp == 4):
	        	lista_escolhida = lista_all
	        	return lista_escolhida
        	elif(resp == 5):
                	lista_escolhida = all_ports
                	return lista_escolhida
       		else:
                	print("Lista Nao Escolhida - Encerrando o PortScan")
        except:
                print("[-] Erro: Valor nao suportado")
