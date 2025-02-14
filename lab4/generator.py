#1
def squares(n):
    for i in range(n + 1):
        yield i * i

n = int(input())
for s in squares(n):
    print(s)

#2
def even_nums(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())
for s in even_nums(n):
    print(s, end=",")    #после последней цифры тоже выходит запятая(


#3
def three_four(n):
    for i in range(n + 1):
        if i%3==0 and i%4==0:
            yield i

n = int(input())
for s in three_four(n):
    print(s)


#4
def squares(a, b):
    for i in range(a, b+1):
        yield i*i

a= int(input())
b = int(input())
for s in squares(a, b):
    print(s)


#5
def nums(n):
    for i in range(n, -1, -1):
        yield i

n= int(input())
for s in nums(n):
    print(s)