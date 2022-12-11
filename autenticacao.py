import hashlib

def signup():
    email=str(input("Digite o seu email: "))
    senha=1
    senha2=2
    while senha!= senha2:
        senha=str(input("Digite a sua senha: "))
        senha2=str(input("Digite a sua senha novamente: "))
        if senha!= senha2:
            print("Senha não possivel. Tente Novamente.")
    with open("contas.txt", "w") as f:
        f.write(email)
        f.write("\n")
        f.write(senha)
    f.close()
    print("O registo foi um sucesso.")

def login():
    email = input("Digite o seu email: ")
    pwd = input("Digite a sua senha: ")
    with open("contas.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if email == stored_email and pwd == stored_pwd:
        print("Login com sucesso!")
    else:
        print("Login não foi possivel!")
