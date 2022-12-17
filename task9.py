a = int(input())
if(a==0 or a==1):
    print("False")
else:

    for i in range(2, a):
        if a%i==0:
            print("False")
            break
    else:
        print("True")
