def faturas(X):
    JJ=len(X)
    Ret=[]
    for i in range(JJ):
        Ret.append(float(input("quanto costou o mês de {0}".format(X[i]))))
    return Ret

def custosMaior(X, Y):
    savMês=""
    sav=0
    for i in range(len(X)):
        if X[i]>sav:
            sav=X[i]
            savMês=Y[i]
    return savMês

def custoMedia(X):
    sav=0
    for i in range(len(X)):
        sav+=X[i]
    sav=sav/len(X)
    return sav

meses=["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

custos=faturas(meses)

print(custosMaior(custos, meses))
print(custoMedia(custos))