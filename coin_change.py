from time import perf_counter
def coin_change(n):
  coins = [20, 10, 5, 1]
  i = 0

  while(n>0):
    if(coins[i] > n):
      i = i+1
    else:
      n = n-coins[i];
if __name__ == '__main__':
  print()  
  sure1 =perf_counter()   
  coin_change(10)
  sure2 = perf_counter()  
  print(' en iyi durum ::',sure2-sure1,'saniye' )
  
  sure1 = perf_counter()
  coin_change(10000)
  sure2 = perf_counter()
  print(' en kotu durum ::', sure2-sure1,'saniye')
  
  sure1 = perf_counter()
  coin_change(5000)
  sure2 = perf_counter()
  print(' ortalama durum ::', sure2-sure1, 'saniye')
  print()
