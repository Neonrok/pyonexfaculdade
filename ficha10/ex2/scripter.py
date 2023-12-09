import os

def escreva():
    
    with open(sefras, "rb") as f:
        base = f.read().decode('utf-8')

    ficheiro=input("qual o ficheiro\n>>")
    
    code=""
    
    if os.path.isfile("./ficha10/ex2/texto/{0}.bin".format(ficheiro)):
        g=open("./ficha10/ex2/texto/{0}.bin".format(ficheiro),"ab+")
    
    else:
        g=open("./ficha10/ex2/texto/{0}.bin".format(ficheiro),"wb+")
    
    escrita=input(">>")
    
    for i in range(len(escrita)):
    
        for j in range(0, len(base), 2):
            c1de=base[j]
    
            if escrita[i] == c1de:
                code+=base[j+1]
    
            elif escrita[i] == " ":
                code+=" "
    
    g.write(code.encode())

def leia():
    f.seek(0)
    
    while True:
        linha=f.readline()
    
        if not linha:
            break
    
        print(linha.decode().strip())



sefras=os.path.join("./ficha10/ex2/sifrado.bin")

cont=True


f=open(sefras, "ab+")

while True:
    Menu=input("MENU\n1-escreva\n2-leia\n0-fim\n\n\t>>")
    match Menu:
        case "1":
            escreva()
        case "2":
            leia()
        case "0":
            print("fim")
            f.close()
            exit()
        case _:
            print("erro")
