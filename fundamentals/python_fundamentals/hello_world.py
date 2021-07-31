# 1. TASK: print "Hello World"
print('Hello World')
# 2. print "Hello Noelle!" with the name in a variable
name = "Patrick"
print('Hello', name)	# with a comma
print('Hello ' + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
favorite_num = 8
print('Hello', name)	# with a comma
print('Hello '+ str(favorite_num))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza chips"
print('I love to eat {} and {}'.format(fave_food1, fave_food2)) # with .format()
print(f'I love to eat {fave_food1} and {fave_food2}') # with an f string
print(f'I love to eat {fave_food1.upper()} and {fave_food2.upper()}') # with an f string
print(f'I love to eat {fave_food1.title()} and {fave_food2.title()}') # with an f string
print(f'I love to eat {fave_food1.title()} and {fave_food2.join(fave_food1)}') # with an f string
print(f'I love to eat {fave_food1.title()} and {fave_food2.split()}') # with an f string