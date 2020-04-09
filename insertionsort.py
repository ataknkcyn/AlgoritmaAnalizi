import random
from time import perf_counter
def insertionsort(array):
    for i in range(1,len(array)):
        v = array[i]
        j = i-1
        while j>=0 and array[j]>v:
            array[j+1]=array[j]
            j-=1
        array[j+1]=v
if __name__ == '__main__':
  array = [i for i in range(0,5000)]
  array1 = [i for i in range(5000,0,-1)]
  array2 = [random.randint(0, 5000) for i in range(0,5000)] 
  print()  
  sure1 =perf_counter()   
  insertionsort(array)
  sure2 = perf_counter()  
  print(' en iyi durum ::',sure2-sure1,'saniye' )
  
  sure1 = perf_counter()
  insertionsort(array1)
  sure2 = perf_counter()
  print(' en kotu durum ::', sure2-sure1,'saniye')
  
  sure1 = perf_counter()
  insertionsort(array2)
  sure2 = perf_counter()
  print(' ortalama durum ::', sure2-sure1, 'saniye')
  print()
    
