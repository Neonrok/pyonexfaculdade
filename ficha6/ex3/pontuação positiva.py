def pontuação_permitida():
    X=int(input("Qual a nota: "))
    while X<0 or X>20:
        X=int(input("Nota invalida por favor escreva entre 0 - 20: "))
    return X

def passou(X):
    nn=0
    while nn<len(X):
        if X[nn]<10:
            del X[nn]
        nn+=1
    return X

Notas=[]

for i in range(10):
    Notas.append(pontuação_permitida())

print(passou(Notas))