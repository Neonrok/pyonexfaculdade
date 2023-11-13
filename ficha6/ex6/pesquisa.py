def searchNumber():
    res=int(input("qual o numero que desejas pesquisar"))
    prov=False
    ret = []
    for i in range(len(listinha)):
        if listinha[i] == res:
            ret.append(i+1)
            prov=True
    if prov==False:
        print("o numero que você escolheu não está na lista")
        exit()
    return ret

listinha=[1,2,3,4,5,6,7,8,9,0,8,6657,55555556,4563,345,76,34,76,85,2346,76,54,12,76,98,56,27,72,95,45,56,76,19,435,6554,24,64]
print("o numero que você pesquisou encontrase na/s posição/ões {0}".format(searchNumber()))
