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


def bubble_sort(char_list):
  n = len(char_list)
  swapped = False

  for i in range(n - 1):
    for j in range(0, n - i - 1):
      if ord(char_list[j]) > ord(char_list[j + 1]):  # Compare ASCII values and change as programmed 'ASCII=>ACIIS'
        char_list[j], char_
