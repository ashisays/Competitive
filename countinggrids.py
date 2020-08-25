""": Given an n × n grid whose
each square is either black (1) or white (0), calculate the number of subgrids whose
all corners are black
"""

def anditems(item,other):
    return [se & so for se,so in zip(item,other)]

def counting_grids(arr,size):
    count = 0
    for i in range(size):
        for j in range(i+1,size):
            tc = anditems(arr[i],arr[j]).count(1)
            count += tc*(tc-1)//2
    return count

def counting_grids1(sq,n):
    sm = 0
    for i in range(n):
        j = i + 1
        while j < n:
            cnt = 0
            for k in range(n):
                if sq[i][k] and sq[j][k]:
                    cnt += 1
            sm += cnt * (cnt - 1) // 2
            j += 1
    print(sm)

sq = []
n = int(input())
for i in range(n):
    sq.append(list(map(int, input().split())))
print(counting_grids1(sq,n))

arr = [[0,1,1,0,1],[0,1,1,0,0],[1,0,0,0,0],[0,1,1,0,1],[0,0,0,0,0]]
print(counting_grids(arr,5))
print(counting_grids1(arr,5))

arr = [[0,1,0,0,1],[0,1,1,0,0],[1,0,0,0,0],[0,1,1,0,1],[0,0,0,0,0]]
print(counting_grids(arr,5))
print(counting_grids1(arr,5))