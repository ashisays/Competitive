"""
You and your friend are playing a card game. You have an ordered deck of N
cards that are numbered from 1 to N where card 1  is placed at the top and card N
 is placed at the bottom.You both perform an operation on the deck until there are at least 2
cards on the deck. You throw away the card on the top and then your friend moves the card that is now on the top of the deck to the bottom.
You are required to determine the number on the final card that is left in the deck.
Input format
First line: A number T
denoting the number of test cases
Each of the next
T lines: A number denoting the number of cards
Output format
For each test case, print the required answer in a new line.
"""
def solve (n):
    print("***************************************** : [%s]"%n)
    res = 1
    # Write your code here
    for i in xrange(n):
        curr = 1 <<i
        print("[%d]"%curr)
        if curr > n:
           break; 
        res = curr
    return res

T = input()
for _ in xrange(T):
    n = input()
    ans = n-solve(n)
    print("_________________________________")
    print("_________________________________")
    if(ans==0):
        print(n);
    else:
        print((2*ans))
