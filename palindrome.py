your_word = input("Enter a word: ")

def is_palindrome(word):
    new_word = ""
    for i in range(len(word) - 1, -1, -1):
        letter = word[i]
        new_word += letter
    return new_word == word
        
if is_palindrome(your_word) is True:
    print("Palindrome")
else:
    print("Not a Palindrome")

# def is_palindrome(word):
#     return word == word[::-1]
#     if word == your_word:
#         is_palindrome(your_word) == True
#     else:
#         is_palindrome(your_word) == False
 
# if is_palindrome(your_word) == True:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")




    

       
