"""
Cyclic shift
A large binary number is represented by a string  of size  and comprises of  and . You must perform a cyclic shift on this string. The cyclic shift operation is defined as follows:

If the string  is , then after performing one cyclic shift, the string becomes .
You performed the shift infinite number of times and each time you recorded the value of the binary number represented by the string. The maximum binary number formed after performing (possibly ) the operation is . Your task is to determine the number of cyclic shifts that can be performed such that the value represented by the string  will be equal to  for the  time.

Input format

First line: A single integer  denoting the number of test cases
For each test case:
First line: Two space-separated integers  and 
Second line:  denoting the string
"""
def cyclicshift(b,k):
  max = int(b,2)
  b = list(b)
  t = 0
  s = 0
  while t< k :
    b = b[1:]+b[:1]
    bi = int("".join(b),2)
    print(max,bi,t,s)
    if bi > max:
      max = bi
      t = 1
    elif bi == max:
      t +=1
    s +=1
  print(s) 

print(cyclicshift("10101",2))



func DoPost(url string, path string) {
	res, err := http.Post(url, "application/json", bytes.NewBuffer(ReadJSON(path)))
	if err != nil {
		fmt.Println("Issue in Post Response:")
		return
	}
	// always close the response-body, even if content is not required
	defer res.Body.Close()
}