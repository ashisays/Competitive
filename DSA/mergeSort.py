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