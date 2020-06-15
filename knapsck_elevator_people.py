"""As an example, consider the following problem: There is an elevator with maximum weight x, and n people who want to get from the ground floor to the top floor.
The people are numbered 0, 1,..., n − 1, and the weight of person i is weight[i].
What is the minimum number of rides needed to get everybody to the top floor?
For example, suppose that x = 12, n = 5, and the weights are as follows:
• weight[0] = 2
• weight[1] = 3
• weight[2] = 4
• weight[3] = 5
• weight[4] = 9
"""

best = [[0,0]]*(1<<5)

def FFD(s, B):
    remain = [B]
    sol = [[]]
    for item in sorted(s, reverse=True):
        for j,free in enumerate(remain):
            if free >= item:
                remain[j] -= item
                sol[j].append(item)
                break
        else:
            sol.append([item])
            remain.append(B-item)
    return sol


print("******************************")
print(FFD([2,3,4,5,9],12))