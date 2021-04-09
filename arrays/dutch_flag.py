'''
This problem is named the "Dutch national flag problem" because the flag of the Netherlands is comprised of the colors red, white, and blue in separate parts. Although we won't be using colors, the premise of the challenge is to develop a sorting algorithm that performs some form of separations of three kinds of elements

To simplify things, we'll use 0s, 1s, and 2s.

Given an array consisting of only 0s, 1s, and 2s, sort the elements in linear time and constant space.

const arr = [2, 0, 1, 0, 2]
dutchNatFlag(arr)
// [0, 0, 1, 2, 2]
'''

def dutch_flag_count(arr):
  counts = [0,0,0]
  for i in arr:
    counts[i] +=1
  index = 0
  for i,val in enumerate(counts):
    val +=index
    while index < val:
      arr[index] = i
      index +=1
  return arr

# print(dutch_flag_count([2,2,2,0,0,1]))

def dutch_flag(arr):
  low,mid,high = 0,0,len(arr)-1
  while mid<=high :
    if arr[mid] ==0 :
      arr[low],arr[mid]=arr[mid],arr[low]
      low +=1
      mid +=1
    elif arr[mid] == 2:
      arr[high],arr[mid]=arr[mid],arr[high]
      high -=1
    else:
      mid +=1
  return arr
    
print(dutch_flag([2,2,2,0,0,1]))