def traingle(n):
    total = n*(n+1)/2
    return total

def close(traingle,n):
    return traingle(n+1)

def sum(func,func1,n):
    print(n,' :',func(n))
    print(n+1,' :',func1(func,n))
    
    sum = func(n) + func1(func,n)
    print('total =',sum)
    
sum(traingle,close,4)