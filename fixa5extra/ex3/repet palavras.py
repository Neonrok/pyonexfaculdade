def repet(X):
    Apalavra=""
    Back=""
    for i in range(len(X)):
        if X[i]==" ":
            NumeroP = X.count(Apalavra)
            if NumeroP>1 and Back.count(Apalavra)<1:
                Back+=Apalavra+" "
            Apalavra=""
        else:
            Apalavra+=X[i]
    return(Back)

cont="Y"

while cont=="Y":
    nome=str(input("escrevai\n\t>> "))
    print(repet(nome))
    cont=str(input("\n\n\n\n\n\tcontinuar(press Y)?\n>> "))