# #Assignment 1 - Calculator

first_number = input("Enter a number: ")
action = input("Enter an operator (+, -, *, /): ")
second_number = input("Enter a second number: ")

def calculator(num_one, operator, num_two):
    if operator == "+":
        return int(num_one) + int(num_two)
    elif operator == "-":
        return int(num_one) - int(num_two)
    elif operator == "*":
        return int(num_one) * int(num_two)
    elif operator == "/":
        return int(num_one) / int(num_two)
    else:
        return "please enter numbers and operator"

answer = calculator(first_number, action, second_number)
print(answer)

#or if you want individual functions for each operation

def add(number1, number2):
   return int(number1) + int(number2)  

def sub(number1, number2):
    return int(number1) - int(number2) 

def mult(number1, number2):
    return int(number1) * int(number2) 

def divide(number1, number2):
    return int(number1) / int(number2) 
    
if action == "+":
    answer = add(first_number, second_number)
    print(f"{first_number} + {second_number} equals {answer}")
elif action == "-":
    answer = sub(first_number, second_number)
    print(f"{first_number} - {second_number} equals {answer}")
elif action == "*":
    answer = mult(first_number, second_number)
    print(f"{first_number} * {second_number} equals {answer}")
elif action == "/":
    answer = divide(first_number, second_number)
    print(f"{first_number} / {second_number} equals {answer}")
else:
    print("please enter numbers and operator")

# #2 Even Odd

your_number = input("Enter a number: ")

def even_odd(number):
    if int(number) % 2 == 0:
        return "Your number is even!"
    elif int(number) % 2 != 0:
        return "Your number is odd!"
    else:
        return "Please enter a whole number"

result = even_odd(your_number)
print(result)

# #3 Write Fizz Buzz

your_number = input("Enter a number: ")

def fizz_buzz(number):
    if (int(number) % 3 == 0) and (int(number) % 5 == 0):
        return "Fizz Buzz"
    elif int(number) % 3 == 0:
        return "Fizz"
    elif int(number) % 5 == 0:
        return "Buzz"
    else:
        return "Your number is not divisible by 3 or 5"

this_answer = fizz_buzz(your_number)
print(this_answer)    