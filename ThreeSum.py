"""
Suppose we have an array of numbers. It stores n integers,
there are there elements a, b, c in the array, such that a + b + c = x.
Find all unique triplets in the array which satisfies the situation.
"""
def threeSum(arr,x):
    arr.sort()
    result = []
    for i in range(len(arr)-2):
        if i >0 and arr[i]==arr[i-1]:
            continue
        j = i+1
        k = len(arr) -1
        while j < k:
            sum = arr[i]+arr[j]+arr[k]
            if sum < x:
                j +=1
            elif sum > x:
                k -=1
            else:
                result.append((arr[i],arr[j],arr[k]))
                #while j<len(arr)-1 and arr[j]==arr[j+1]: j+=1
                #while k>0 and arr[k] == arr[k-1]: r -=1
                j +=1
                k -=1
    return  result


"""
The 2Sum problem
Given an array of integers a[n] and an integer number k as a target sum
Determine whether there is a pair of elements a[i] and a[j] that sums exactly to k
"""

def twoSumHasing(arr,x):
    result = []
    table = {}
    for i in range(len(arr)):
        comp = x - arr[i]
        if comp in table:
            print ("The pairt with sum equal to %d is : [%d,%d]" %(x,arr[i],comp))
            result.append((arr[i],comp))
        table[arr[i]] = arr[i]
    return result

def twoSum(arr,x):
    arr.sort()
    result = []
    i = 0
    j = len(arr)-1
    while(i<j):
        sum = arr[i]+arr[j]
        if sum < x:
            i +=1
        elif sum > x:
            j -=1
        else:
            result.append((arr[i],arr[j]))
            i +=1

    return  result

print("*******************Three Sum ***************")
print(threeSum([-1,0,1,2,-1,-4],0))
print(threeSum([1,2,3,4,5,6,7,8,9,0],8))

print("*******************Two Sum Hashing***************")
print(twoSumHasing([-1,0,1,2,-1,-4],0))
print(twoSumHasing([1,2,3,4,5,6,7,8,9,0,1],8))

print("*******************Two Sum Two Pointers***************")
print(twoSum([-1,0,1,2,-1,-4],0))
print(twoSum([1,2,3,4,5,6,7,8,9,0,1],8))
