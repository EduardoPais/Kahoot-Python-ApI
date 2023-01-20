import os  
import time
import openpyxl
reiniciar = '\033[0m'
vermelho = '\033[31m'
verde = '\033[32m'
laranja = '\033[33m'
azul = '\033[34m' 
def signup():
    os.system("cls")
    print(azul+"\n************* Signup **************"+reiniciar)
    email_sig=str(input("Digite o seu email: "))
    last_char= email_sig[-1]
    firt_char= email_sig[0]
    if last_char=="@" or firt_char=="@":
        signup()
    elif not email_sig.__contains__("@"):
        signup()
    senha="a"
    senha2="b"
    a=0
    b=0
    c=0
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
    n=1
    x=0
    book = openpyxl.load_workbook(r"contas.xlsx")
    sh = book.active
    while x!=1:
        cell = sh.cell(row=n,column=1)
        cell2 = sh.cell(row=n,column=2)
        if cell.value == email_sig:
            print(vermelho+"Usuario já existente!"+reiniciar)
            time.sleep(1)
            os.system("python main.py")
        if cell.value != None:
            n+=1
        else:
            cell.value=email_sig
            cell2.value=senha
            x=1
    book.save(r"contas.xlsx")
    print(verde+"\nO registo foi um sucesso."+reiniciar)
    time.sleep(1)

def login():
    os.system("cls")
    print(azul+"\n************* Login **************"+reiniciar)
    n2=1
    x2=0
    global email_log
    email_log=str(input("Digite o seu email: "))
    book = openpyxl.load_workbook(r"contas.xlsx")
    sh = book.active
    while x2!=1:
        cell = sh.cell(row=n2,column=1)
        cell2 = sh.cell(row=n2,column=2)
        if cell.value == email_log:
            x2=1  
        if cell.value == None:
            print(vermelho+"\nConta não existente!"+reiniciar)
            x2=1
            time.sleep(1)
            signup()
        else:
            n2+=1
    n2-=1
    senha=str(input("Digite a sua senha: "))
    cell2 = sh.cell(row=n2,column=2)
    if cell2.value==senha:
        print(verde+"\nLogin com sucesso!"+reiniciar)
        time.sleep(1)
    else:
        print(vermelho+"\nLogin não foi possivel!"+reiniciar)
        time.sleep(1)
        login()
    book.save(r"contas.xlsx")