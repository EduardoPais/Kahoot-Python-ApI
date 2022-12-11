import os
from autenticacao import login
from autenticacao import signup
os.system("cls")
while 1:
    print("********** Sistema Login **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Digite o que pretende fazer: "))
    if ch == 1:
        signup()
        login()
    elif ch == 2:
        login()
        break
    elif ch == 3:
        exit()
    else:
        print("Numero não valido. Tente novamente.")

tipo=str(input("É professor ou aluno?"))

while tipo!="professor" and "aluno" and "Professor" and "Aluno":
    tipo=str(input("Resposta não valida. Escreva novamente."))

if tipo.lower() =="professor":
    print("adeus")

else:
    print("olá")