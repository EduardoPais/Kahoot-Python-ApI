import os  
import time
import openpyxl


def signup():
    os.system("cls")
    print("\n************* Signup **************")
    email_sig=str(input("Digite o seu email: "))
    last_char= email_sig[-1]
    firt_char= email_sig[0]
   #validaçao do email
    if last_char=="@" or firt_char=="@":
        signup()
    elif not email_sig.__contains__("@"):
        signup()
    senha="a"
    senha2="b"
    a=0
    b=0
    c=0
   #validaçao da senha
    while len(senha)>=13 or len(senha)<=7 or senha!=senha2 or c!=1 or a!=1 or b!=1:
        print("\nPassword tem de conter entre 8 e 12 caracteres, conter no mínimo uma maiúscula, uma minúscula e um número.")
        senha=str(input("Digite a sua senha: "))
        senha2=str(input("Digite a sua senha novamente: "))
        for char in senha:
            if char.isnumeric():
                a=1
            if char.islower():
                b=1
            if char.isupper():
                c=1
    #guardar email e senha num ficheiro exel
    n=1
    x=0
    book = openpyxl.load_workbook(r"contas.xlsx")
    sh = book.active
    while x!=1:
        cell = sh.cell(row=n,column=1)
        cell2 = sh.cell(row=n,column=2)
        #verifica se uma conta com o mesmo email já existe
        if cell.value == email_sig:
            print("Usuario já existente!")
            time.sleep(1)
            signup()
        if cell.value != None:
            n+=1
        else:
            cell.value=email_sig
            cell2.value=senha
            x=1
    book.save(r"contas.xlsx")
    print("\nO registo foi um sucesso.")
    time.sleep(1)

def login():
    os.system("cls")
    print("\n************* Login **************")
    n2=1
    x2=0
    global email_log
    email_log=str(input("Digite o seu email: "))
    book = openpyxl.load_workbook(r"contas.xlsx")
    sh = book.active
    while x2!=1:
        cell = sh.cell(row=n2,column=1)
        cell2 = sh.cell(row=n2,column=2)
        #procura o email
        if cell.value == email_log:
            x2=1  
        if cell.value == None:
            print("\nConta não existente!")
            x2=1
            time.sleep(1)
            signup()
        else:
            n2+=1
    #passa se o email existir
    n2-=1
    senha=str(input("Digite a sua senha: "))
    cell2 = sh.cell(row=n2,column=2)
    #verifica se a senha coincide
    if cell2.value==senha:
        print("\nLogin com sucesso!")
        time.sleep(1)
    else:
        print("\nLogin não foi possivel!")
        time.sleep(1)
        login()
    book.save(r"contas.xlsx")