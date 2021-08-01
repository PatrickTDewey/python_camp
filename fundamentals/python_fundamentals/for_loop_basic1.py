# Basic Print all integers from 0 to 150
for i in range(0, 151):
    print( int(i))

# Multiples of Five print all the multiples of 5 from 5 to 1,000
for i in range(5, 1001, 5):
    print(i)

# Print integers 1 to 100 if divisble by 5 print "Coding" instead, if divisible by 10 print "Coding Dojo"
for i in range(1, 100):
    if i % 10 == 0:
        print('Coding Dojo')
    elif i % 5 == 0:
        print('Coding')
    else:
        print(i)

# Add odd integers from 0 to 500,000 and print the final sum
odd_sum = 0
for i in range(1, 500000):
    if i % 2 != 0:
        odd_sum += i
print(odd_sum)

# Countdown by fours
for i in range(2018, 0, -4):
    print(i)

# lowNum highNum mult
low_num = 2
high_num = 9
mult = 3
for i in range(low_num, high_num + 1):
    if i % mult == 0:
        print(i)

some_list = [1, 2, 4, 5, 6]
some_list += [2]
print(some_list)

x = ''

if not x:
    print(True)