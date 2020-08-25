import  math as mt

def terenarySearch(l,r,key,arr):
    if r >=l :
        mid1 = l+(r-l) // 3
        mid2 = r-(r-l) // 3
        if arr[mid1] == key:
            return mid1
        elif arr[mid2] == key:
            return mid2
        elif key < arr[mid1]:
            return terenarySearch(l,mid1-1,key,arr)
        elif key > arr[mid2]:
            return terenarySearch(mid2+1,r, key, arr)
        else:
            return terenarySearch(mid1 + 1, mid2-1, key, arr)
    return -1


l, r, key = 0, 9, 5
ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

p = terenarySearch(l, r, key, ar)
# Print the result
print("Index of", key, "is", p)

key = 17
# Search the key using ternarySearch
p = terenarySearch(l, r, key, ar)
# Print the result
print("Index of", key, "is", p)