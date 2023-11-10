import random
def generate_numbers(liminf, limsup, nr):
    chave=[]
    while len(chave) < nr:
        num=random.randint(liminf,limsup)
        if num not in chave:
            chave.append(num)
    return chave
cont="Y"
while cont.upper()=="Y":
    print("A chave do euromilhões é {0} e {1}".format(generate_numbers(1,50,5), generate_numbers(1,12,2)))
    cont=input("deseja continuar?(Y/N)")