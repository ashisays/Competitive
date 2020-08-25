"""
We have an array arr[0 . . . n-1]. We should be able to efficiently
find the minimum value from index L (query start) to R (query end) where 0 <= L <= R <= n-1.
Consider a situation when there are many range queries.
https://www.geeksforgeeks.org/sparse-table/
"""

import math
def buildSparseTable(arr, n):

    for i in range(n):
        lookup[i][0] = arr[i]
    j = 1
    while (1 <<j) <= n:
        ##compute all minimum value for interval of 2
        i = 0
        while (i + (1<<j)-1) < n:
            if lookup[i][j-1] < lookup[i +(1<<(j-1))][j-1]:
                lookup[i][j] = lookup[i][j-1]
            else:
                lookup[i][j] = lookup[i+(1<<(j-1))][j-1]
            i +=1
        j+=1

def query(L,R):
    # Find highest power of 2 that is smaller
    # than or equal to count of elements in
    # given range. For [2, 10], j = 3
    j = int(math.log2(R - L + 1))
    # Compute minimum of last 2^j elements
    # with first 2^j elements in range.
    # For [2, 10], we compare arr[lookup[0][3]]
    # and arr[lookup[3][3]],
    if lookup[L][j] <= lookup[R - (1 << j) + 1][j]:
        return lookup[L][j]
    else:
        return lookup[R - (1 << j) + 1][j]


a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
n = len(a)
MAX = 500

# lookup[i][j] is going to store minimum
# value in arr[i..j]. Ideally lookup table
# size should not be fixed and should be
# determined using n Log n. It is kept
# constant to keep code simple.
lookup = [[0 for i in range(MAX)]
          for j in range(MAX)]

buildSparseTable(a, n)
print(query(0, 4))
print(query(4, 7))
print(query(7, 8))
