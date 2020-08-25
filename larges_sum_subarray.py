"""
Given an integer array arr[], the task is to find the largest sum contiguous subarray of non-negative elements and return its sum.

Examples:

Input: arr[] = {1, 4, -3, 9, 5, -6}
Output: 14
Explanation:
Subarray [9, 5] is the subarray having maximum sum with all non-negative elements.

Input: arr[] = {12, 0, 10, 3, 11}
Output: 36
"""

def find_sum_subarray(arr):
    i = 0
    j = 1
    max_sum = 0
    sum = 0
    sum += arr[i]
    while i<j:
        if sum > max_sum:
            max_sum = sum

        if j == len(arr):
            break
        elif arr[j] <0:
            j +=1
            if j < len(arr)-1:
                i = j
                j +=1
                sum = arr[i]
            elif j == len(arr)-1:
                sum = arr[j]
                j +=1
            else:
                break
        else:
            sum += arr[j]
            j +=1

    return max_sum


def find_continuous_subarray(arr):
    i = 0
    j = 1
    max_len = 0
    len_cont = 1

    for i in range(1,len(arr)):
        if arr[i-1] < arr[i]:
            len_cont += 1
        else:
            if max_len < len_cont:
                max_len = len_cont
            len_cont = 1
    return max_len


print("Sum :%s" %find_sum_subarray([1,3,-1,5]))
print("Sum :%s" %find_sum_subarray([1, 4, -3, 9, 5, -6]))
print("Sum :%s" %find_sum_subarray([12, 0, 10, 3, 11]))

print("len :%s" %find_continuous_subarray([1,3,-1,5]))
print("len :%s" %find_continuous_subarray([1, 4, -3, 9, 5, -6]))
print("len :%s" %find_continuous_subarray([12, 0, 10, 3, 11]))
print("len :%s" %find_continuous_subarray([1, 56, 58, 57, 90, 92, 94, 93, 91, 45]))