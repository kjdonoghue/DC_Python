
number= int(input("Enter a number: "))


def factorial(num):
    total = 1
    if num <= 0:
        print("please enter a number greater or equal to 1")
    elif num > 1:
        for i in range(1,num+1):
            total *= i
        print(f"The factorial of {num} is {total}")
factorial(number)
