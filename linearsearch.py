from time import perf_counter

def linearSearch(n,array):
    for i in array:
        if i is n:
            return True
    return False

if '__main__' == __name__:
  array = [i for i in range(0,5000)]
  print()  
  sure1 =perf_counter()   
  linearSearch(0,array)
  sure2 = perf_counter()  
  print(' en iyi durum ::',sure2-sure1,'saniye' )
  
  sure1 = perf_counter()
  linearSearch(4999,array)
  sure2 = perf_counter()
  print(' en kotu durum ::', sure2-sure1,'saniye')
  
  sure1 = perf_counter()
  linearSearch(2500,array)
  sure2 = perf_counter()
  print(' ortalama durum ::', sure2-sure1, 'saniye')
  print()


    
