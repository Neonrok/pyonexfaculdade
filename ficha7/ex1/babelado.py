def conta(X, Y):
    Z=[]
    for i in range(X):
        Z.append([])
        for e in range(Y):
            Z[i].append(int(input("escplha o numero da coluna {0} da linha {1}\n>>".format(i+1, e+1))))
    return Z

Linhas=3
Colunas=3

trva=conta(Linhas, Colunas)

for i in range(len(trva)):
    print("")
    for e in range(len(trva)):
        print(trva[i][e], " ", end="")

for i in range(len(trva)):
    print("")
    for e in range(len(trva)):
        print(trva[e][i], " ", end="")
print("")