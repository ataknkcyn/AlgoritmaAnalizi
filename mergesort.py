from time import perf_counter 
import random
def merge(a, start, middle, end):
  size_of_temp1 = (middle-start)+1
  size_of_temp2 = (end-middle)

  temp1 = [0]*size_of_temp1
  temp2 = [0]*size_of_temp1

  for i in range(0, size_of_temp1):
    temp1[i] = a[start+i]

  for i in range(0, size_of_temp2):
    temp2[i] = a[middle+1+i]

  i=0
  j=0
  k=start

  while (i < size_of_temp1 and j < size_of_temp2):
    if (temp1[i] < temp2[j]):
      a[k] = temp1[i]
      i = i+1
    else:
      a[k] = temp2[j]
      j = j+1
    k = k+1

  
  while (i<size_of_temp1):
    a[k] = temp1[i]
    k = k+1
    i = i+1

  while (j<size_of_temp2):
    a[k] = temp2[j]
    k = k+1
    j = j+1

def merge_sort(a, start, end):
  if (start < end):
    middle = (start+end)//2
    merge_sort(a, start, middle)
    merge_sort(a, middle+1, end)
    merge(a, start, middle, end)

if __name__ == '__main__':
  bestcase = [i for i in range(0,5000)]
  worstcase= [i for i in range(5000,0,-1)]
  avaragecase=[random.randint(0,5000) for i in range(0,5000)]
  print()  
  sure1 =perf_counter()   
  merge_sort(bestcase,0,4999)
  sure2 = perf_counter()  
  print(' en iyi durum ::',sure2-sure1,'saniye' )
  
  sure1 = perf_counter()
  merge_sort(worstcase,0,4999)
  sure2 = perf_counter()
  print(' en kotu durum ::', sure2-sure1,'saniye')
  
  sure1 = perf_counter()
  merge_sort(avaragecase,0,4999)
  sure2 = perf_counter()
  print(' ortalama durum ::', sure2-sure1, 'saniye')
  print()
