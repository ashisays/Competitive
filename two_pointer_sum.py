"""
consider a problem where we are given an
array of n positive integers and a target sum x, and we want to find a subarray whose
sum is x or report that there is no such subarray
e.g. [1,3,2,5,1,1,2,3]
"""

def find_sum_subarray(arr,x):
    i = 0
    j = 1
    sum = 0
    sum += arr[i]
    while i<j:
        while sum <= x and j <= len(arr):
            if sum == x:
                print("%s,%s,%s"%(i,j,arr[i:j]))
            if j < len(arr):
                sum += arr[j]
            j +=1
        else:
            if i < len(arr):
                sum -= arr[i]
            i += 1



print(find_sum_subarray([1,3,2,2,5,1,1,2,3,1,4,5,6,1,1,2,6,2,1,7,6,2],8))
print(find_sum_subarray([1,3,2,2,5,1,1,2,3,1,4,5,6,1,1,2,6,2,1,7,6,2],8))
