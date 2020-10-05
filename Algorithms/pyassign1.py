# #Assignment 1 - Calculator

first_number = int(input("Enter a number: "))
action = input("Enter an operator (+, -, *, /): ")
second_number = int(input("Enter a second number: "))

def calculator(num_one, operator, num_two):
    if operator == "+":
        return num_one + num_two
    elif operator == "-":
        return num_one - num_two
    elif operator == "*":
        return num_one * num_two
    elif operator == "/":
        return num_one / num_two
    else:
        return "please enter numbers and operator"

answer = calculator(first_number, action, second_number)
print(answer)

# or if you want individual functions for each operation

def add(number1, number2):
   return number1 + number2

def sub(number1, number2):
    return number1 - number2

def mult(number1, number2):
    return number1 * number2 

def divide(number1, number2):
    return number1 / number2 
    
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

your_number = int(input("Enter a number: "))

def even_odd(number):
    if (number % 2 == 0):
        return "Your number is even!"
    elif (number % 2 != 0):
        return "Your number is odd!"
    else:
        return "Please enter a whole number"

result = even_odd(your_number)
print(result)

# #3 Write Fizz Buzz

your_number = int(input("Enter a number: "))

def fizz_buzz(number):
    answer = ""
    if (number % 3 == 0) and (number % 5 == 0):
        answer = "Fizz Buzz"
    elif (number % 3) == 0:
        answer = "Fizz"
    elif (number % 5) == 0:
        answer = "Buzz"
    else:
        answer = "Your number is not divisible by 3 or 5"

    return answer

this_answer = fizz_buzz(your_number)
print(this_answer)    
