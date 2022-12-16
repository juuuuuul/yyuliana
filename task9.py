a = int(input())
for i in range(2, a):
    if a%i==0:
        print("Составное")
        break
else:
    print("Простое")
