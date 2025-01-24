#'hello' is the same as "hello".
#Quotes inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello, World!"
print(a[1]) #output: e

for x in "banana":
  print(x) 

d = "Hello, World!"
print(len(d)) #length of a string (13)

txt = "The best things in life are free!"
print("free" in txt) #True

#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

c = " Hello, World! "
print(c.strip()) # returns "Hello, World!"

age = 36
text = f"My name is John, I am {age}"
print(text)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) #The price is 59.00 dollars

txt = "We are the so-called \"Vikings\" from the north."