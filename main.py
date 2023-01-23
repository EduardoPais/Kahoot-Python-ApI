import os  
from autenticacao import login
from autenticacao import signup
from questionarios import criar
from questionarios import responder
from podio import podio
from podio import lista_testes
import time

reiniciar = '\033[0m'
vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'

while 1:
    
    os.system("cls")
    print(azul+"********** Sistema Login **********"+reiniciar)
    print("1.Signup\n2.Login\n"+vermelho+"3.Exit"+reiniciar)
    ch=input("Digite o que pretende fazer: ")
    
    if  ch.isnumeric():
        ch = int(ch)        
        if ch == 1:
            signup()
            login()
            break
        elif ch == 2:
            login()
            break
        elif ch == 3:
            os.system("cls")
            print(vermelho+"*********Saiu*********"+reiniciar)
            time.sleep(2)
            exit()
    else:
        print(vermelho+"Numero não valido. Tente novamente."+reiniciar)
while 1:
    os.system("cls")
    print(azul+"***********Menu***********"+reiniciar+"\n1.Criar\n2.Responder\n3.Podio\n4.Testes\n"+vermelho+"5.Exit"+reiniciar)
    tipo=(input("Digite o que pretende fazer: "))
    if tipo.isnumeric():
        tipo=int(tipo)
        if tipo ==1:
            criar()
        elif tipo ==2:
            responder()
        elif tipo==3:
            podio()
        elif tipo==4:
            lista_testes()
        elif tipo ==5:
            os.system("cls")
            print(vermelho+"*********Saiu*********"+reiniciar)
            time.sleep(2)
            exit()
    else:
        print(vermelho+"Numero não valido. Tente novamente."+reiniciar)
