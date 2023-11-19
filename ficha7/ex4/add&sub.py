def soma(X,Y):
    Z=[]
    for i in range(len(X)):
        Z.append([])
        for j in range(len(X[i])):
            D=X[i][j]
            S=Y[i][j]
            Z[i].append(S+D)
    return Z

def subt(X,Y):
    Z=[]
    for i in range(len(X)):
        Z.append([])
        for j in range(len(X[i])):
            D=X[i][j]
            S=Y[i][j]
            Z[i].append(D-S)
    return Z

A=[[5,4], [0,2], [1,-1]]
B=[[0,-2], [5,-3], [-1,0]]
ciclo=True

while ciclo==True:
    escolha=int(input("\t\tMENU\n\t1- Somar Matrizes\n\t2- Sobtrair Matrizes\n\t0- Terminar\n\nescolha\n>>"))
    
    match escolha:
        case 1:
            print(soma(A,B))
        case 2:
            print(subt(A,B))
        case 0:
            print("fim")
            ciclo=False
        case _:
            print("erro")