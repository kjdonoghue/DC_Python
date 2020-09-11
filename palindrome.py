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
