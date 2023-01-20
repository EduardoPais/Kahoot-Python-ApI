import os  
from autenticacao import login
from autenticacao import signup
from questionarios import criar
from questionarios import responder
from podio import podio
from podio import lista_testes

while 1:
    os.system("cls")
    print("********** Sistema Login **********")
    print("1.Signup\n2.Login\n3.Exit")
    ch = int(input("Digite o que pretende fazer: "))
    #escolhe uma das funçoes e valida a resposta
    if ch == 1:
        signup()
        login()
        break
    elif ch == 2:
        login()
        break
    elif ch == 3:
        os.system("cls")
        print("*********Saiu*********")
        exit()
    else:
        print("Numero não valido. Tente novamente. ")



while 1:
    os.system("cls")
    print("***********Menu***********\n1.Criar\n2.Responder\n3.Podio\n4.Testes\n5.Exit")
    tipo=int(input("Digite o que pretende fazer: "))

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
        print("*********Saiu*********")
        exit()
    else:
        print("Numero não valido. Tente novamente. ")