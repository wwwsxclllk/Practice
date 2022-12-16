imp = (input("Введите ip в формате: xxx.xxx.xxx.xxx : "))
b = []
for i in range(12):
    a = list(imp.replace(":",""))
    b.append(bin(int(a[i])).replace("0b" ,""))
    print(*b, sep="")