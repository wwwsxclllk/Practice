imp = (input("Введите MAC в формате: AAAA:BBBB:CCCC : "))
b = []
for i in range(12):
    a = list(imp.replace(":",""))
    b.append(bin(int(a[i])).replace("0b",""))
    print(*b)