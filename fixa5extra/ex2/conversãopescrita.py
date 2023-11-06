def convertText(X):
    S=""
    for i in range(len(X)):
        Letra=X[i]
        
        if Letra=="1":
            S+="um"
        elif Letra=="2":
            S+="dois"
        elif Letra=="3":
            S+="tres"
        elif Letra=="4":
            S+="quatro"
        elif Letra=="5":
            S+="cinco"
        elif Letra=="6":
            S+="seis"
        elif Letra=="7":
            S+="sete"
        elif Letra=="8":
            S+="oito"
        elif Letra=="9":
            S+="nove"
        elif Letra=="0":
            S+="zero"
        else:
            S+=Letra
    return(S)

nome=str(input("escrevai\n>> "))
you=convertText(nome)
print(you)