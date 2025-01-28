from functions import is_palindrome, guess_the_number

word = input("Enter a word or phrase to check if it's a palindrome: ")
if is_palindrome(word):
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome!")

guess_the_number()

