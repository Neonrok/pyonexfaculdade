import os

def escreva():
    
    ficheiro=input("qual o ficheiro\n>>")
    
    if os.path.isfile("./ficha10/ex2/texto/{0}.bin".format(ficheiro)):
        g=open("./ficha10/ex2/texto/{0}.bin".format(ficheiro),"ab+")
    
    else:
        g=open("./ficha10/ex2/texto/{0}.bin".format(ficheiro),"wb+")
    
    escrita=input(">>")
    
    code = script(escrita)
    
    print(escrita, code)
    g.write(code.encode())
    g.close()


def script(X):

    code=""
    nlista=False

    with open(sefras, "rb") as f:
        base = f.read().decode('utf-8')
    for i in range(len(X)):
        for j in range(0, len(base), 2):
            MoreX = X[i]
            c1de=base[j]
            print(MoreX, c1de)
            if MoreX == str(c1de):
                print(X[i], c1de, base[j+1])
                code += base[j+1]
                nlista=True
            elif X[i] == " ":
                print("else", X[i], c1de)
                code+=" "
                nlista=True
        if nlista==False:
            code+=X[i]
    return code
    

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
