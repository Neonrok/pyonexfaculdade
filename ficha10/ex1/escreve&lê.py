import os

def escreva():
    escrita=input(">>")+"\n"
    f.write(escrita.encode())

def leia():
    f.seek(0)
    while True:
        linha=f.readline()
        if not linha:
            break
        print(linha.decode().strip())

local=os.path.join("C:\\Base\\repositorios\\pyonexfaculdade\\ficheiros\\blábláblá.bin")
cont=True


f=open(local, "ab+")

while cont==True:
    Menu=input("MENU\n1-escreva\n2-leia\n0-fim\n\n\t>>")
    match Menu:
        case "1":
            escreva()
        case "2":
            leia()
        case "0":
            print("fim")
            cont=False
        case _:
            print("erro")

f.close()