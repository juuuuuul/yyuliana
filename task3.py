a=int(input("Введите a"))
b=int(input("Введите b"))
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print(b)
