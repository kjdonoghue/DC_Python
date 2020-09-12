#Largest Element

numbers = [2,1,5,4,3]

def find_largest_element(list,):
  largest_element = numbers[0]
  for num in numbers:
    if num > largest_element:
      largest_element = num

  return largest_element

largest_element = find_largest_element(numbers)

print(f"The largest element is {largest_element}")

#Smallest Element

def find_smallest_element(list):
  smallest_element = numbers[0] 
  for num in numbers:
    if num < smallest_element:
        smallest_element = num

  return smallest_element

smallest_element = find_smallest_element(numbers)

print(f"The smallest element is {smallest_element}")