"""
The Hamming distance hamming(a, b) between two strings a and b of equal length
is the number of positions where the strings differ. For example,
hamming(01101, 11001) = 2.
"""

def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    return str(bin(x^y)).count('1')

print("THe first String is  : " +str(bin(93)))
print("THe Second String is : " +str(bin(73)))
print("The Hamming Dist is  :   %s" %hammingDistance(93, 73))

