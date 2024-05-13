def delete_element(array, index):

  if 0 <= index < len(array):
    
    return array[:index] + array[index + 1:]
  else:
    print("Invalid index.")
    return array


array = [3, 7, 1, 9, 4]
new_array = delete_element(array, 2)
print(new_array)  # Output should be : [3, 7, 9, 4]

new_array = delete_element(array, -1)
print(new_array)  #Checked
