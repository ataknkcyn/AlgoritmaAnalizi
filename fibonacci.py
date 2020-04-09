def Fib(n):
    fib = [1,1]    
    for i in range(2,n+2):
        fib.append(fib[i-1] + fib[i-2]) 
    return fib[len(fib)-1]

if '__main__' == __name__:
    print(Fib(3))
