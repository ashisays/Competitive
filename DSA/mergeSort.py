def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        a,b,c = 0,0,0
        while a < len(left) and b < len(right):
            if left[a] <= right[b]:
                arr[c] = left[a]
                a +=1
            else:
                arr[c] = right[b]
                b +=1
            c +=1

        while a < len(left):
            arr[c] = left[a]
            a +=1
            c +=1

        while b < len(right):
            arr[c] = right[b]
            b +=1
            c +=1
    return arr

print(mergeSort([1,4,3,2,5,9,8,6,7]))

def binarySearch(arr,value):
    first = 0
    last = len(arr)-1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2
        if arr[mid] == value:
            found = True
        else:
            if arr[mid] > value:
                last = mid -1
            else:
                first = mid+1
    return found

print(binarySearch([1,2,3,4,57,8,9],6))
print(binarySearch([1,2,3,4,57,8,9],0))
print(binarySearch([1,2,3,4,57,8,9],1))


