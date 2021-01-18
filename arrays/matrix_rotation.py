def matrixRotaion(m):
  n = len(m[0])
  for i in range(n//2):
    for j in range(i,n-i-1):
      temp = m[i][j]
      m[i][j] = m[n-1-j][i]
      m[n-1-j][i] = m[n-i-1][n-j-1]
      m[n-i-1][n-j-1] =m[j][n-i-1]
      m[j][n-i-1] = temp
  return m

matrix = [
          [1 ,2 ,3 ,4],
          [5 ,6 ,7 ,8],
          [9 ,10,11,12],
          [13,14,15,16]
          ]

rm = matrixRotaion(matrix)
for i in rm:
  print(i)