import os
 
sefras = os.path.join("./ficha10/ex2/sifrado.bin")
 
def escreva():  # write()
    ficheiro = input("qual o ficheiro\n>>")
    if os.path.isfile("./ficha10/ex2/texto/{0}.bin".format(ficheiro)):
        g = open("./ficha10/ex2/texto/{0}.bin".format(ficheiro), "ab")
    else:
        g = open("./ficha10/ex2/texto/{0}.bin".format(ficheiro), "wb")
 
    escrita = input(">>")
 
    code = script(escrita)
    print(escrita, code)
 
    code = code+"\n"
    g.write(code.encode('utf-8'))
    print("___\n"+code)
    g.close()
 
 
def script(X):
    code=""
    
    with open(sefras, "rb") as f:
        base = f.readlines()
    
    charli = {chr(i+97): base[i].decode('utf-8').strip() for i in range(26)}
    charli[" "] = " "
    
    for char in X:
        if char in charli:
            code += charli[char]
        else:
            code += char
    
    return code
 
 
def leia(): 
   with open(sefras, 'rb') as file:
      data = file.readlines()
 
   for linha in data:
      print(linha.decode('utf-8').strip())
 
 
 
while True:
   Menu = input("MENU\n1-escreva\n2-leia\n0-fim\n\n\t>>")
   match Menu:
      case "1":
         escreva()  
      case "2":
         leia()  
      case "0":
         print("fim")  
         exit()
      case _:
         print("erro")
