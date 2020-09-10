number = int(input("Enter a number: "))

def prime(num):
    if num == 1:
        return False
    elif num == 2 :
        return True;
    else:
        for i in range(2,num):
            if(num % i == 0):
                return False
            else:
                return True             

result = prime(number)

if result == True:
    print("Prime Number")
else:
    print("Not a Prime Number")
