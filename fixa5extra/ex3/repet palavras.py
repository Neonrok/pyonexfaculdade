def repet(X):
    S=""
    Back=""
    for i in range(len(X)):
        if X[i]==" ":
            B = X.count(S)
            if B>1 & Back.count(S)<1:
                Back+=S+" "
            S=""
        else:
            S+=X[i]
    return(Back)

cont="Y"

while cont=="Y":
    nome=str(input("escrevai\n>> "))
    print(repet(nome))
    cont=str(input("\n\n\n\n\n\tcontinuar(press Y)?\n>> "))