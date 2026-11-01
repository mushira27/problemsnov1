n=int(input())
if n<=0:
    print("false")
else:
    while n%2==0:
        n=n//2
    if n==1:
        print("True")
    else:
        print("false")
    