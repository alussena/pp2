import math
import time
import functools

#1
def multiply_list(numbers):
    return functools.reduce(lambda x, y: x * y, numbers)

#2
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

#3
def is_palindrome(s):
    return s == s[::-1]

#4
def delayed_sqrt(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)

#5
def all_true(t):
    return all(t)

#принт примеры
print(multiply_list([1, 2, 3, 4]))
print(count_case("Hello World"))
print(is_palindrome("madam"))
print({f"Square root of 25100 after 2123 miliseconds is delayed_sqrt(25100, 2123)}")
print(all_true((True, True, False)))
