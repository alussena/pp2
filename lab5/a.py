#1
import re
with open(r"C:\Users\Админ\OneDrive\Desktop\git\pp2-1\lab5\row.txt", 'r', encoding='utf-8') as file:
    text_to_match = file.read()
    print(text_to_match)

    text_to_match = file.read()

pattern = r"ab*"
result = re.findall(pattern, text_to_match)
print(result)

#2 
pattern = r"ab{2,3}"
result = re.findall(pattern, text_to_match)
print(result)

#3
pattern = r'\b[a-z]+_[a-z]+\b'
result = re.findall(pattern, text_to_match)
print(result)

#4
pattern = r'\b[A-Z][a-z]+\b'
result = re.findall(pattern, text_to_match)
print(result)

#5
pattern = r'a.*b'
result = re.findall(pattern, text_to_match)
print(result)

#6
pattern = r'[ ,.]'
result = re.sub(pattern, ':', text_to_match)
print(result)

#7
def snake_to_camel(snake_str):
    return ''.join(word.capitalize() for word in snake_str.split('_'))

pattern7 = r'\b[a-z]+(?:_[a-z]+)+\b'
matches7 = re.findall(pattern7, text_to_match)
camel_case_results = [snake_to_camel(m) for m in matches7]
print(camel_case_results)

#8
pattern = r'[A-Z][a-z]*'  #Write a Python program to split a string at uppercase letters.
result = re.findall(pattern, text_to_match)
print(result)

#9. Write a Python program to insert spaces between words starting with capital letters.
pattern = r'([a-z])([A-Z])'
result = re.sub(pattern, r'\1 \2', text_to_match)
print(rsult)

#10.Write a Python program to convert a given camel case string to snake case

def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

pattern = r'\b[A-Z][a-zA-Z]+\b'
matches = re.findall(pattern, text_to_match)
snake_case_results = [camel_to_snake(m) for m in matches]
print(snake_case_results)
