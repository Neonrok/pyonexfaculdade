def ordem():
    invert=1
    f.seek(0)
    consult= f.readlines()
    print("data\thora\ttemperatura\n--------------------------")
    for line in consult:
        if invert==1 or invert==2:
            print(line.strip(), end="")
            invert+=1
        else:
            print("\t", line.strip())
            invert=1

def convert():
    registro=0
    numeros=[]
    maior=-255
    menor=+999999
    f.seek(0)
    consult= f.readlines()
    for i in range(len(consult)):
        if (i+1)%3==0:
            numeros.append(consult[i])
    for j in range(len(numeros)):
        numero=numeros[j]
        numero=numero.strip()
        numero=int(numero)
        if numero>maior:
            maior=numero
        if numero<menor:
            menor=numero
        registro+=numero
    print(maior)
    print(menor)
    print(registro/len(numeros))



cont=True
f=open("temperaturas.txt", "r")
while cont==True:
    escolha=input("MENU\n1-estorico\n2-registros diferentes\n0-sair\n\n>>")
    match escolha:
        case "1":
            ordem()
        case "2":
            convert()
        case "0":
            print("Fim")
            cont=False
        case _:
            print("erro")

f.close()