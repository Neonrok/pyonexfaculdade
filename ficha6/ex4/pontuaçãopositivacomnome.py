def pontuação_permitida():
    X=int(input("Qual a nota: "))
    while X<0 or X>20:
        X=int(input("Nota invalida por favor escreva entre 0 - 20: "))
    return X

def nome_do_participante():
    X=str(input("qual o nome do participante: "))
    return X

def passou(X):
    nn=0
    while nn<len(X):
        if X[nn]<10:
            del X[nn]

        nn+=1
    return X

def Nomepassou(X,Y):
    nn=0
    while nn<len(X):
        if Y[nn]<10:
            del X[nn]

        nn+=1
    return X

Notas=[]
Nomes=[]

for i in range(10):
    Nomes.append(nome_do_participante())
    Notas.append(pontuação_permitida())

print(Nomepassou(Nomes, Notas))
print(passou(Notas))