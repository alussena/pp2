#1
def grams_to_ounces(grams):
    ounces = grams * 28.3495231
    return ounces

grams = float(input())
print(grams_to_ounces(grams))

#2
def farenheit_to_cantigrade(F):
    c = (5/9)*(F-32)
    return c
F = int(input())
print(farenheit_to_cantigrade(F))

#3
def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    return chickens, rabbits

numheads = 35
numlegs = 94
chickens, rabbits = solve(numheads, numlegs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")

#4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0,5)+1):
        if n % i == 0:
            return False
        return True

def filter_prime(nums):
    return [n for n in nums if is_prime(n)]

nums = [10, 15, 17, 19, 20, 23] #list(map(int, input().split()))
print(filter_prime())

#5
from itertools import permutations
def print_permutations(string):
    perms = permutations(string)
    for perm in perms:
        print("".join(perm))

s = input()
print_permutations(s)

#6
def reverse_sentence(sentence):
    words = sentence.split()  
    reversed_words = words[::-1]  
    return " ".join(reversed_words)  

s = input()
print(reverse_sentence(s))

#7
def has_33(nums):
    print(nums)
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#8
def spy_game(nums):
    code = [0, 0, 7]
    index = 0

    for num in nums:
        if num == code[index]:
            index += 1
        if index == len(code):
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

#9
import math
def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

radius = float(input())
print(sphere_volume(radius))

#10
def unique_elements(l):
    unique_lst = []
    for item in l:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

numbers = [1, 2, 2, 3, 4, 4, 5]
print(unique_elements(numbers))

#11
def is_palindrome(s):
    return s == s[::-1]

user_input = input()
if is_palindrome(user_input):
    print("YES")
else:
    print("NO")

#12
def histogram(lst):
    for num in lst:
        print('*' * num)

user_input = input()
numbers = list(map(int, user_input.split()))
histogram(numbers)
#histogram([4, 9, 7])

#13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    number_to_guess = random.randint(1, 20)

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    guess_count = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guess_count += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            # Correct guess
            print(f"Good job, {name}! You guessed my number in {guess_count} guesses!")
            break

guess_the_number()




