def deli(s):
  switch = 0
  counta = 0
  countb = 0
  curr = s[0]
  count = 1
  lastcount = None
  for i in range(1,len(s)):
    if s[i] != curr:
      curr = s[i]
      if i %2 == 0:
        countb += count
        lastcount = counta
      else:
        counta += count
        lastcount = countb
      count = 1
      switch +=1
    else:
      count +=1
  min1 = min(counta,countb) + count 
  return min(max(counta,countb),min1)

print(deli("AABBBB"))
print(deli("BAAABAB"))
print(deli("BBABAA"))