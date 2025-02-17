from www import is_palindrome

word = input("Enter: ")
if is_palindrome(word):
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome!")

