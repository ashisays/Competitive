def solve (n):
    print("***************************************** : [%s]"%n)
    res = 1
    # Write your code here
    for i in xrange(n):
        curr = 1 <<i
        print("[%d]"%curr)
        if curr > n:
           break; 
        res = curr
    return res

T = input()
for _ in xrange(T):
    n = input()
    ans = n-solve(n)
    print("_________________________________")
    print("_________________________________")
    if(ans==0):
        print(n);
    else:
        print((2*ans))
