"""
problem is to find a path from the upper-left corner to the lower-right corner
of an n × n grid, with the restriction that we may only move down and right. Each
square contains an integer, and the path should be constructed so that the sum of the
values along the path is as large as possible.
[3], 7 , 9 ,2  ,7
[9],[8], 3 , 5 ,5
1  ,[7],[9],[8],[5]
3  ,8  ,6  ,4 ,[10]
6  ,3  ,9  ,7 ,[8]

"""
def sum(yn,xn):
    m = 0
    first = {}
    sum = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    for y in range(xn):
        for x in range(yn):
            if x > -1 and y > -1:
                s1 = sum[y][x-1]
                s2 = sum[y-1][x]
                if s1 < s2:
                    sum[y][x] = s2 + A[y][x]
                    first[sum[y][x]] = (y-1,x)
                else:
                    sum[y][x] = s1 + A[y][x]
                    first[sum[y][x]] = (y , x-1)
                if m < sum[y][x]:
                    m = sum[y][x]
    while m:
        r, c = first[m]
        if r == 0 and c == 0:
            print("Print Path Traversed: [%s,%s] %s" % (r, c, A[r][c]))
            break
        else:
            print("Print Path Traversed: [%s,%s] %s" %(r,c,A[r][c]))
            m = sum[r][c]
    # return sum
# Driver Code
A = [[3,7,9,2,7], [9,8,3,5,5], [1,7,9,8,5],[3,8,6,4,10],[6,3,9,7,8]]
print(sum(5,5))