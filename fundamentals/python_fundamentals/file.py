import random
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
    File  line 121, in <module>
    fruit.append('raspberry')
    AttributeError: 'tuple' object has no attribute 'append'
"""
# fruit.pop(1)
"""
    Traceback (most recent call last):
    File line 129, in <module>
    fruit.pop(1)
    AttributeError: 'tuple' object has no attribute 'pop'
"""

xy = 50
if xy > 50:
    print('Greater Than 50')
else:
    print('Less Than or Equal to 50')

#class throwError:
"""
    File  line 146
        class EmptyClass:
        ^
    IndentationError: expected an indented block
"""

class EmptyClass:
    pass # Pass used when we know we are going to want a code block to do something but don't know what we want it to do yet. 

ishungry = True
has_freckles = False

age = 28 #stores int
weight = 185.3 #stores float
name_two = 'SomeWeirdStringyName' #stores string
immutable_data_type = ('This', 'Tuple', 'Is', 'Immutable', 4)
for x in immutable_data_type:
    print(x)

empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

print(type(3j))

int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))
print(random.randint(2,5))

name = "Zen"
my_int = 4
print("My name is", name)
print('My name is ' + name)
print('My int is', my_int)
# print('My int is ' + my_int)
"""
    Traceback (most recent call last):
    File "/home/gecko/coding/python/fundamentals/python_fundamentals/file.py", line 194, in <module>
    print('My int is ' + my_int)
    TypeError: can only concatenate str (not "int") to str
"""
# Type Casting or Type Conversion
#print("Hello" + 42)			    # output: TypeError
print("Hello " + str(42))		    # output: Hello 42

total = 35
user_val = "26"
# total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61

# String Interpolation
first_name_one = "Zen"
last_name_one = "Coder"
age_one = 27
print(f"My name is {first_name_one} {last_name_one} and I am {age_one} years old.")

# Old format method

print("My name is {} {} and I am {} years old.".format(first_name_one, last_name_one, age_one))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age_one, first_name_one, last_name_one))
# output: My name is 27 Zen and I am Coder years old.

# % Formatting
hw = "Hello %s" % "world" 	# with string
py = "I love Python %d" % 3.222 #with int value (this only returns 3)
print(hw, py)
# output: Hello world I love Python 3

print("My name is %s and I'm %d" % (first_name_one, age_one))		# or with variables
# output: My name is Zen and I'm 27

string_to_play_with = 'The slow black dog jumps over the lazy brown fox slow did I say slow'
print(string_to_play_with.title()) #Capitalizes the first character in word
print(string_to_play_with.upper()) #Uppercase all the WORDS
print(string_to_play_with.lower()) #lowercases them
print(string_to_play_with.count('slow')) # counts all occurences of substrings in a string returns the number
print(string_to_play_with.split('b')) # Rerturns a list of values where string is split at given character, default = space
print(string_to_play_with.split()) # Rerturns a list of values where string is split at given character, default = space
print(string_to_play_with.find('black')) # returns the index of the start of the first occuence of substring within string.
print(string_to_play_with.isalnum()) # returns bool if every character (spaces included) return alpha numeric symbols --> spaces & punctuation will return false
# .isdigit() islower() isupper() .isalpha() are similar methods
print(string_to_play_with.join(ninjas)) # returns a string that is all string within our set in this case the list ninjas
print(string_to_play_with.endswith('slow')) # returns a boolean based on whether the last characters of string match substring


list_to_mess_with = [1, 'cheese', 'broccoli', True, ('tuple', 'in', 'list'), {'dict': 'in_list', 'true/false': True}]

for x, element in enumerate(list_to_mess_with, start=10):
    print(x, element)

li = [1, 8, 3, 5, 4, 6, 7, 2, 9, 10]

def func(x):
    return x**x
print(list(map(func, li)))
print([func(x) for x in li if x % 2 == 0])
# newList = []
# for x in li:
#     newList.append(func(x))

# print(newList)
print(min(li))
print(sorted(li))
# print(sorted(list_to_mess_with))
list_to_mess_with.extend(li)
print(list_to_mess_with)
print(li.index(8))


# dictionaries
context = {
    'questions': [
        { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
        { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
        { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
        { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
    ]
}
another_dict = {
    'name': 'Patrick',
    'age': 28,
    'height': "5'10",
    'favorite_func': map
}
# cmp() removed in Python 3.x
def add(a):
    return a + a
print(len(context))
for x in context['questions']:
    print(len(x['content']))

    
for x in context['questions']:
    print(x['content'].upper())

    
for x in context['questions']:
    print(type(x))
my_copy = context.copy()
context.clear()
print(context)
print(my_copy['questions'][0]['id'])

print('questions' in my_copy)
print(my_copy.items())
my_copy.update(another_dict)
print(my_copy)
print(my_copy.values())

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
     print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
print('values *********************')
for val in capitals.values():
     print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

