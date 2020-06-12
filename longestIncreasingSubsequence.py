length = {}
def solve (n):
    """The longest increasing subsequence in an array of n elements is a maximum-length
sequence of array elements that goes from left to right, and each element in the
sequence is larger than the previous element.
    e.g [6,2,5,1,7,4,8,3]
    have The longest increasing subsequence of
     [2, 5, 7, 8]
    """
    m = 0
    for k in range(len(n)):
        length[k] = 1
        for i in range(k):
            if n[i] < n[k]:
                # breakpoint()
                length[k] = max([length[k],length[i]+1])
        if m < length[k]:
            m = length[k]
    return m
# T = input()
# for _ in range(T):
#     n = input("comma seperated list of num.e.g. 1,2,3")
#     n = n.split(",")
#     print(solve(n))
#
print(solve([6,2,5,1,7,4,8,3]))