def uniqueCharacters(str):   
    # Assuming string can have characters
    # a-z this has 32 bits set to 0
    checker = 0
    for i in range(len(str)):
        bitAtIndex = ord(str[i]) - ord('a')
        # If that bit is already set in
        # checker, return False
        if ((bitAtIndex) > 0):
            if ((checker & ((1 << bitAtIndex))) > 0):
                return False                
            # Otherwise update and continue by
            # setting that bit in the checker
            checker = checker | (1 << bitAtIndex)
    # No duplicates encountered, return True
    return True

# Write your code here
def UpUP(c):
	if 97 < ord(c) < 122:
		c = chr(ord(c)-30)
	return c

def checkUp(s):
    s[0] = UpUP(s[0])
    for i in range(1,len(s)):
        if s[i] == " ":
            if (i != len(s)-1):
                s[i+1] = UpUP(s[i+1])
    print(s)
    return s


def PerfPerf(s, t):
    print(s)
    print(t)
    ssi = 0
 
    for ch in t:
        print(f"ch is {ch}")
        if ch == s[ssi]:
            print(f"s[ssi] is : {s[ssi]}")
            ssi += 1
            if ssi == len(s):
                break
 
    return ssi
 

def permutation(s,s1):
  if len(s)!= len(s1):
    return False
  si = 0
  si1 = 0
  for i in range(len(s)):
        b = ord(s[i]) - ord('a')
        si = si | (1 << b)
        b1 = ord(s1[i]) - ord('a')
        si1 = si1 | (1 << b1)
  return si == si1

def urlify(s):
  ls = list(s)
  i = 0
  while i < len(ls):
    if ls[i] == " ":
      j = i+1
      while j < len(ls):
        if ls[j] != " ":
          while i < j:
            ls[i] = "%20"
            i +=1
          break
        j +=1
    i +=1
  return "".join(ls)

def strComp(s):
  ls = len(s)
  if ls == 0:
    return s
  ch = s[0]
  c = 1
  cs = ""
  for i in range(1,ls):
    if ch != s[i]:
      cs +=f"{ch}{c}"
      c = 1
      ch = s[i]
    else:
      c +=1
  cs +=f"{ch}{c}"

  if len(cs) > ls:
    return s
  return cs

def editAway(s,s1):
  ss = set(s)
  ss1 = set(s1)
  if len(ss - ss1) > 1:
    return False
  return True



if __name__ == '__main__':
    # in1 = ["GeekforGeeks","abc10d","a b c"]
    # for a in in1 :
    #   if (uniqueCharacters(a)):
    #     print(f"The string {a}, has unique characters")
    #   else :
    #     print(f"The string {a}, has duplicate characters")
    # s = input()
    # print(checkUp(s))
    # S = "digger"
    # T = "biggerdiagram"
    # print(PerfPerf(S, T))
    #permutation
    #print(permutation("ashi","ishac"))
    ##URLIfy
    ##print(urlify("Mr Ashish  P    "))
    # print(strComp("aaabaaacccc"))
    # print(strComp("abac"))
    print(editAway("pale","ale"))
    print(editAway("pale","bake"))