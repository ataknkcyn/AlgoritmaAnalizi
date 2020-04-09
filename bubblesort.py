from time import perf_counter 
import random
def bubble_sort(a):
      for i in range(0, len(a)):
        for j in range(0, len(a)-i-1):
          if (a[j] > a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]
#        print(a[i], end=' ')
            
if __name__ == '__main__':
  bestcase = [i for i in range(0,5000)]
  worstcase= list(reversed([i for i in range(0,5000)]))
  avaragecase=[random.randint(0,5000) for i in range(0,5000)]
  print()  
  sure1 =perf_counter()   
  bubble_sort(bestcase)
  sure2 = perf_counter()  
  print(' en iyi durum ::',sure2-sure1,'saniye' )
  
  sure1 = perf_counter()
  bubble_sort(worstcase)
  sure2 = perf_counter()
  print(' en kotu durum ::', sure2-sure1,'saniye')
  
  sure1 = perf_counter()
  bubble_sort(avaragecase)
  sure2 = perf_counter()
  print(' ortalama durum ::', sure2-sure1, 'saniye')
  print()
