def bubble_sort(arr):
 
  n = len(arr)
  
  swapped = True
  while swapped:
    swapped = False
    for i in range(n - 1):
      
      if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        swapped = True

  return arr

array = ['A', 'S', 'C', 'I', 'I']
sorted_array = bubble_sort(array)
print(sorted_array)  # checked
