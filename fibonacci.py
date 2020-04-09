from time import perf_counter
import time
def Fib(n):
    fib = [1,1]    
    for i in range(2,n+2):
        fib.append(fib[i-1] + fib[i-2]) 
    return fib[len(fib)-1]

if '__main__' == __name__:
  print()  
  sure1 =perf_counter()   
  Fib(100)
  sure2 = perf_counter()  
  print(' en iyi durum ::',sure2-sure1,'saniye' )
  
  sure1 = perf_counter()
  Fib(10000)
  sure2 = perf_counter()
  print(' en kotu durum ::', sure2-sure1,'saniye')
  
  sure1 = perf_counter()
  Fib(5000)
  sure2 = perf_counter()
  print(' ortalama durum ::', sure2-sure1, 'saniye')
  print()
