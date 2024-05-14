def search_and_count(numbers, target):

  count = 0
  for num in numbers:
    if num == target:
      count += 1

  return count

def merge_sort(numbers):
 
  if len(numbers) <= 1:
    return numbers

  # Divide the list into two halves
  mid = len(numbers) // 2
  left = merge_sort(numbers[:mid])
  right = merge_sort(numbers[mid:])

  # Merge the sorted halves
  merged = []
  i = j = 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1

  # Add any remaining elements from either half
  merged += left[i:]
  merged += right[j:]

  return merged

def main():

  numbers = []
  while True:
    number_str = input("Enter a number (or 'done' to finish): ")
    if number_str.lower() == 'done':
      break
    try:
      number = int(number_str)
      numbers.append(number)
    except ValueError:
      print("Invalid input. Please enter a number.")

  if not numbers:
    print("No numbers entered.")
    return

  target_str = input("Enter the number to search for: ")
  try:
    target = int(target_str)
  except ValueError:
    print("Invalid input. Please enter a number.")
    return

  count = search_and_count(numbers, target)
  if count == 0:
    print(f"The number {target} is not present in the list.")
  else:
    print(f"The number {target} appears {count} times in the list.")

  # Sort the list using merge sort
  sorted_numbers = merge_sort(numbers.copy())  
  print("The sorted list is:", sorted_numbers)

if __name__ == "__main__":
  main()
