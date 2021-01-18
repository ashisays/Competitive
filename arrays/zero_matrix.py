def zero_matrix(m):
  zero = []
  r = len(m)
  c = len(m[0])

  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == 0:
        zero.append((1,j))
  rz = []
  cz = []
  for val in zero:
    if val[0] not in rz:
      for i in range(c):
        m[val[0]][i] = 0
      rz.append(val[0])
    if val[1] not in cz:
      for i in range(r):
        m[i][val[1]] = 0
      cz.append(val[1])
  return m

m = [[1 ,2 ,3 ,4 ,5 ],
     [6 ,0 ,8 ,0  ,10],
     [11,12,13,14,0]]

zm = zero_matrix(m)
for i in zm:
  print(i)
#     [1 ,0 ,3 ,0 ,0 ],
#     [0 ,0 ,0 ,0 ,0 ],
#     [11,0 ,13,0 ,0 ]]