def main():
  numbers = []
  while True:
    number_str = input("Enter a number (or 'done' to finish): ")
    if number_str.lower() == 'done':
      break
    try:
      number = float(number_str)  # Handle both integers and decimals
      numbers.append(number)
    except ValueError:
      print("Invalid input. Please enter a number.")

  # Search for target number
  if not numbers:
    print("No numbers entered.")
  else:
    target_str = input("Enter a number to search: ")
    try:
      target = float(target_str)
      count = numbers.count(target)
      if count > 0:
        print(f"The number {target} appears {count} times in the list.")
      else:
        print(f"The number {target} is not present in the list.")
    except ValueError:
      print("Invalid input. Please enter a number to search.")

if __name__ == "__main__":
  main()
