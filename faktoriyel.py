from time import perf_counter 
def faktoriyel(n):
    if n<=1 : 
        return 1
    else:
        return faktoriyel(n-1)*n

if __name__ == '__main__':
  print()  
  sure1 =perf_counter()   
  faktoriyel(5)
  sure2 = perf_counter()  
  print(' en iyi durum ::',sure2-sure1,'saniye' )
  
  sure1 = perf_counter()
  faktoriyel(50)
  sure2 = perf_counter()
  print(' en kotu durum ::', sure2-sure1,'saniye')
  
  sure1 = perf_counter()
  faktoriyel(25)
  sure2 = perf_counter()
  print(' ortalama durum ::', sure2-sure1, 'saniye')
  print()


    
