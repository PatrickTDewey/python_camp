# Single Line Comments Are made like this
"""
Multi-Line Comments
are made like this.
"""

my_new_favorite_language = 'Python' # variable declaration, initiliaze string

num1 = 42 # varaible declaration, initiliaze int
num2 = 2.3 # variable declaration, initiliaze float
boolean = True # variable declaration, init bool
string = 'Hello World' # variable declaration, init string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, init list (array)
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # varaible declaration, init dictionary (object)
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, init tuple? A collection which is ordered and unchangeable
print(type(fruit)) # prints the value type of the variable fruit which is <class 'tuple'>
print(pizza_toppings[1]) # prints the item at the 1 index of the pizza toppings list which is 'Sausage'
pizza_toppings.append('Mushrooms') # Appends 'Mushrooms' to the pizza_toppings list
print(person['name']) # prints the value of the key 'name' from the dictionary person --> John
person['name'] = 'George' # changes the value for the key 'name' in dict person from John to George
person['eye_color'] = 'blue' # adds the key 'eye_color' to the person dict with value 'blue'
print(fruit[2]) # prints fruit at 2 index --> banana

if num1 > 45: # num1 = 42 
    print("It's greater") # doesn't run now
else:
    print("It's lower") # prints it's lower since num1 = 42

if len(string) < 5: #len(string) = 11
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!") #prints Just Right!

for x in range(5):
    print(x) # 0, 1, 2, 3, 4
for x in range(2,5):
    print(x) # 2, 3, 4
for x in range(2,10,3): 
    print(x) # 2 , 5, 8 --> 8+3 then loop stops, optional argument at the end to increment by number other than 1 in this case 3
x = 0
while(x < 5): #while loop
    print(x) # 0, 1, 2, 3, 4
    x += 1 #add increment at bottom

pizza_toppings.pop() #pops 'Mushrooms'
pizza_toppings.pop(1) #pops 'Sausage

print(person) # prints {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': 'blue'}
person.pop('eye_color') #pops eye_color key value pair from dict
print(person) # prints {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue #goes back to top of for loop starting now 'Sausage'
    print('After 1st if statement') # Prints After 1st if statement three times
    if topping == 'Olives': # 4th index == 'Olives' for loop breaks
        break #stops for loop

def print_hello_ten_times():
    for num in range(10): # num = 0, 0 -> 9, num = num + 1
        print('Hello') # prints hello ten times when print_hello_ten_times() called

print_hello_ten_times() # prints Hello ten times

def print_hello_x_times(x): #function defined print_hello_x_times(x) takes parameter x
    for num in range(x): # init for loop in range of argument given
        print('Hello') # prints hello

print_hello_x_times(4) #prints hello 4 times

def print_hello_x_or_ten_times(x = 10): # adds a default parameter to function that will unless specified = 10
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() # prints hello 10 times
print_hello_x_or_ten_times(4) # prints hello 4 times


"""
Bonus section
"""

# print(num3)
# num3 = 72 
""" 
    Traceback (most recent call last):
    File  line 85, in <module>
    print(num3)
    NameError: name 'num3' is not defined
"""
#fruit[0] = 'cranberry'
#print(fruit)
"""
    Traceback (most recent call last):
    File line 93, in <module>
    fruit[0] = 'cranberry'
    TypeError: 'tuple' object does not support item assignment
"""
# print(person['favorite_team'])
"""
    Traceback (most recent call last):
    File line 101, in <module>
    print(person['favorite_team'])
    KeyError: 'favorite_team'
"""
#print(pizza_toppings[7])
"""
    Traceback (most recent call last):
    File line 108, in <module>
    print(pizza_toppings[7])
    IndexError: list index out of range
"""
#   print(boolean)
"""
    File line 115
    print(boolean)
    IndentationError: unexpected indent
"""
# fruit.append('raspberry')
# print(fruit)
"""
    Traceback (most recent call last):
    File "/home/gecko/coding/python/fundamentals/python_fundamentals/file.py", line 121, in <module>
    fruit.append('raspberry')
    AttributeError: 'tuple' object has no attribute 'append'
"""
# fruit.pop(1)
"""
    Traceback (most recent call last):
    File "/home/gecko/coding/python/fundamentals/python_fundamentals/file.py", line 129, in <module>
    fruit.pop(1)
    AttributeError: 'tuple' object has no attribute 'pop'
"""