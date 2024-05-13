from 1_array import as array_of_numbers,     # I have only problem of importing the other array class b/c  I have checked my code and its working
arr=array_of_numbers

def merge_sort(arr):
  
  if len(arr) <= 1:
    return arr  
  
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]

  
  left = merge_sort(left)
  right = merge_sort(right)

  
  return merge(left, right)

def merge(left, right):
 

  merged = []
  i = 0  

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1

  
  merged += left[i:]
  merged += right[j:]

  return merged

#for check up 

my_list = [10,12,3,4,8,5,6]
sorted_list = merge_sort(my_list)

print("Original list:", my_list)
print("Sorted list:", sorted_list)
