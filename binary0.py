"""
Count all 0s which are blocked by 1s in binary matrix
Given Binary matrix. Task is count all zeros which are surrounded by one (may not be immediate neighbor).
Note: here we are only taking four direction up, left, down, right.
Examples:

Input :  Int M[][] = {{ 0, 1, 1, 0},
                      { 1, 0, 0, 1},
                      { 0, 1, 0, 1},
                      { 1, 0, 1, 1}}
Output : 3
Explanation : All zeros which are surrounded
by 1 are (1, 1), (1, 2) and (2, 2)
"""

Row = 4
Col = 5
r = [0, 0, 1, -1 ]
c = [1, -1, 0, 0 ]


def isSafe(x, y, M):
    if (x >= 0 and x < Row and y >= 0 and y < Col):
        if M[x][y] == 0:
            return True
    return False

def dfs(x,y,matrix):
    #visited every node.
    matrix[x][y]=1
    for k in range(len(matrix)):
        if isSafe(x+r[k],y+c[k],M)