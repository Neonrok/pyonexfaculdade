def print_park():
    for i in range(len(logares)):
        vazio=0
        for j in range(len(logares[i])):
            if logares[i][j] == 1:
                vazio+=1
        print("linha {0} tem {1}".format(i,  5-vazio))

def entrar():
    for i in range(len(logares)):
        for j in range(len(logares[i])):
            if logares[i][j] == 0:
                logares[i][j] = 1
                return i, j
    return -1, -1

def sair(i, j):
    if logares[i][j]!= 1:
        print('lugar vazio, verifique coordenadas')
    else:
        logares[i][j] = 0

logares=[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
Espasso=[[]]


fim=False

while fim==False:
    L=input("\t\tMenu\n1 - Entrada de veículo\n2 - Saída de carro\n3 - Estado do Parque\n0 - Sair\n\n>>")
    match L:
        case "1":
            x, y = entrar()
            print("Veiculo no lugar", x+1, y+1)
            #print(inicial(logares, Espasso))
        case "2":
            x = int(input("coluna\n>>"))
            y = int(input("lugar\n>>"))
            sair(x-1, y-1)
        case "3":
            print_park()
        case "0":
            print("fim")
            fim=True
        case _:
            print("erro")
