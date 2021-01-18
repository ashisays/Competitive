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
 

if __name__ == '__main__':
    # in1 = ["GeekforGeeks","abc10d","a b c"]
    # for a in in1 :
    #   if (uniqueCharacters(a)):
    #     print(f"The string {a}, has unique characters")
    #   else :
    #     print(f"The string {a}, has duplicate characters")
    # s = input()
    # print(checkUp(s))
    S = "digger"
    T = "biggerdiagram"
  
    print(PerfPerf(S, T))
