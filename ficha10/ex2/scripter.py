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
    print("___\n"+code)
    g.close()


def script(X):
    
    code=""

    with open(sefras, "rb") as f:
        base = f.read().decode('utf-8')
    mapping = {base[i]: base[i+1] for i in range(0, len(base), 2)}  # Cria um mapeamento de caracteres para caracteres codificados

    for char in X:
        if char in mapping:  # Se o caractere está no mapeamento
            code += mapping[char]  # Adicione o caractere codificado ao código
        elif char == " ":  # Se o caractere é um espaço
            code += " "
        else:  # Se o caractere não está no mapeamento
            code += char
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
