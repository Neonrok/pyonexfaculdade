num=[]
npm=0
for i in range(10):
    pergunta=int(input("ponha o {0}º numero\n>>".format(i+1)))
    num.append(pergunta)

npm=sum(num)/10

for i in range(10):
    if npm<num[i]:
        print(num[i], end="")
        print(" ",end="")
print("")
