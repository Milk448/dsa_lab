def search_and_count(numbers, target):
  count = 0
  for num in numbers:
    if num == target:
      count += 1

  return count

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

if __name__ == "__main__":
  main()
