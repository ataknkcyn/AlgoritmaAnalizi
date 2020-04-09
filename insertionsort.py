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
  array = [i for i in range(0,15000)]
  array = [10,30,40,304,10,2,3,4,5,123]
  array1 = [i for i in range(15000,0,-1)]
  array2 = [random.randint(0, 10000) for i in range(0,15000)] 
  print()  
  sure1 =perf_counter()   
  insertionsort(array)
  sure2 = perf_counter()  
  print(' en iyi durum ::',sure2-sure1,'saniye' )
  
  sure1 = perf_counter()
 ## insertionsort(array1)
  sure2 = perf_counter()
  print(' en kotu durum ::', sure2-sure1,'saniye')
  
  sure1 = perf_counter()
 # insertionsort(array2)
  sure2 = perf_counter()
  print(' ortalama durum ::', sure2-sure1, 'saniye')
  print()
    
