def incerirpaises():
    pais=input("país\n>>")
    continente=input("continente\n>>")
    escreve="{0}\n{1}\n".format(pais, continente)
    f.write(escreve)

def ConsultarPaises():
    invert=True
    f.seek(0)
    consult= f.readlines()
    print("Paíse\tContinente\n--------------------------")
    for line in consult:
        if invert==True:
            print(line.strip(), end="")
            invert=False
        else:
            print("\t", line.strip())
            invert=True

def porContinente():
    invert=True
    escolha= input("qual o continente\n>>") +"\n"
    f.seek(0)
    consult= f.readlines()
    print("Paíse\tContinente\n--------------------------")
    for i in range(len(consult)):
        if i+1<len(consult):
            if invert==True and consult[i+1] == escolha:
               print(consult[i].strip(), end="")
               invert=False
            elif consult[i]==escolha:
               print("\t", consult[i].strip())
               invert=True

def numeroporcotinente():
    escolhidos=[]
    f.seek(0)
    consult= f.readlines()
    print("Continente\tnºPaíses\n--------------------------")
    for i in range(len(consult)):
        if (i+1)%2==0 and escolhidos.count(consult[i])==0:
            escolhidos.append(consult[i])
            conta=0
            for j in range(len(consult)):
                if escolhidos[-1]==consult[j]:
                    conta+=1
            print("{0}\t{1}".format(escolhidos[-1], conta))

f=open("paises.txt", "a+")
cont=True
while cont==True:
    Menu= input("\tMENU\n1 - Inserir Paises\n2 - Consultar Paises\n3 - Consultar Continentes\n4 - Consultar nº Paises\n0 - Sair\n\n>>")

    match Menu:
        case "1":
            incerirpaises()
        case "2":
            ConsultarPaises()
        case "3":
            porContinente()
        case "4":
            numeroporcotinente()
        case "0":
            print("fim")
            cont=False
        case _:
            print("erro")

f.close()