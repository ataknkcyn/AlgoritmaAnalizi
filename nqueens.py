from time import perf_counter
def control(i, j, board, N):
  # j sutunu kontrol
  for k in range(1, i):
    if(board[k][j] == 1):
      return False

  # ust sag diagonal kontrol
  k = i-1
  l = j+1
  while (k>=1 and l<=N):
    if (board[k][l] == 1):
      return False
    k=k+1
    l=l+1

  # ust sol diagonal kontrol
  k = i-1
  l = j-1
  while (k>=1 and l>=1):
    if (board[k][l] == 1):
      return False
    k=k-1
    l=l-1

  return True

def n_queen(row, n, N, board):
  if (n==0):
    return True

  for j in range(1, N+1):
    if(control(row, j, board, N)):
      board[row][j] = 1

      if (n_queen(row+1, n-1, N, board)):
        return True

      board[row][j] = 0 #backtracking
  return False

if __name__ == '__main__':
      board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
      board2=[[0,0,0],[0,0,0],[0,0,0]]
      board3 =  [[0,0,0,0,0,0,0,0,0,0]
                ,[0,0,0,0,0,0,0,0,0,0]
                ,[0,0,0,0,0,0,0,0,0,0]
                ,[0,0,0,0,0,0,0,0,0,0]
                ,[0,0,0,0,0,0,0,0,0,0]
                ,[0,0,0,0,0,0,0,0,0,0]
                ,[0,0,0,0,0,0,0,0,0,0]
                ,[0,0,0,0,0,0,0,0,0,0]
                ,[0,0,0,0,0,0,0,0,0,0]]
      print()  
      sure1 =perf_counter()   
      
      n_queen(1, 2, 2, board2)
      sure2 = perf_counter()  
      print(' en iyi durum ::',sure2-sure1,'saniye' )
      
      sure1 = perf_counter()
      n_queen(1, 7, 7, board3)      
      sure2 = perf_counter()
      print(' en kotu durum ::', sure2-sure1,'saniye')
      
      sure1 = perf_counter()

      n_queen(1, 4, 4, board)
      sure2 = perf_counter()
      print(' ortalama durum ::', sure2-sure1, 'saniye')
      print()
