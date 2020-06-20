"""
Let sumq (a, b) (“range sum query”) denote the sum of array values in a range [a, b].
The prefix sum array can be constructed in O(n) time. Then, since the prefix sum
array contains all values of sumq (0, k), we can calculate any value of sumq (a, b) in
O(1) time using the formula
sumq (a, b) = sumq (0, b) − sumq (0, a − 1)
"""

def sumQuery(arr,a,b):
    ps = []
    sum = 0
    for i in range(len(arr)):
        sum +=arr[i]
        ps.append(sum)
    if a>0:
        return (ps[b] - ps[a-1])
    else:
        return ps[b]

print("****************“range sum query”****************************")
arr = [1,3,4,8,6,1,4,2]
print("Range sum for array %s is: %s" %(arr,sumQuery(arr,3,6)))
print("Range sum for array %s is: %s" %(arr,sumQuery(arr,0,6)))