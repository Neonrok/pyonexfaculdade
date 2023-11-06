num=int (input("qual numero desejas converter\n>> "))
rom=""
if num>=4000 and num<0:
    print("um numero que seja menor que 4000 e maior que 0")
    exit()

while num>1000:
    num-=1000
    rom+="M"

if num>900:
    num-=900
    rom+="CM"
elif num>500:
    num-=500
    rom+="D"
elif num>=400:
    num-=400
    rom+="CD"

while num>100:
    num-=100
    rom+="C"

if num>90:
    num-=90
    rom+="XC"
elif num>50:
    num-=50
    rom+="L"
elif num>=40:
    num-=40
    rom+="XL"

while num>10:
    num-=10
    rom+="X"

if num==9:
    num-=9
    rom+="IX"
elif num==5:
    num-=5
    rom+="V"
elif num==4:
    num-=4
    rom+="IV"

while num>=1:
    num-=1
    rom+="I"

print(rom)