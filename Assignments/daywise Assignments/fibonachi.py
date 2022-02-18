def fibo(n):
    if n<=0:
       return "wrong input"
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(10))