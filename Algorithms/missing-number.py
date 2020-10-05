#Find The Missing Number

list_numbers = [0,1,2,3,4,5,6,8,9]

def find_missing_numbers(list):
  for i in list:
    if (list[i] + 1) != list[i+1]:
      return (list[i]+1)
  
missing_number = (find_missing_numbers(list_numbers))
print(f"The missing number is {missing_number}")
