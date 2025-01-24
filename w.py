print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

print(bool("Hello")) #True
print(bool(15)) #True

#False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") #YES!

#isinstance() function, which can be used to determine if an object is of a certain data type
x = 200
print(isinstance(x, int)) #True