def substring(s):
  count = 0
  ss = ""
  for i in s:
    if i in ss:
      ss = i
      count +=1
    else:
      ss = ss+i
  if len(ss) > 0 :
    count +=1
  return count

print(substring("abacdec"))