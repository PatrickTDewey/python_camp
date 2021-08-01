x = [ [5,2,3], [10,8,9] ] 
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# change value 10 in x to 15
for li in x:
    for list_item in range(len(li)):
        print(li[list_item])
        if li[list_item] == 10:
            li[list_item] = 15
print(x)
# changed back to 10
x[1][0] = 10
print(x)

# another way to word 13 - 17
for i in range(len(x)):
    for j in range(len(x[i])):
        print (x[i][j])

# practice with enumerate for fun
for i, v in enumerate(x[0]):
    print(i, v)

# change last_name jordan to bryant
students[0]['last_name'] = 'Bryant'
print(students[0])

# Change name messi to andres
sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

# change value 20 -> 30
z[0]['y'] = z[0]['x'] + z[0]['y']
print(z[0])

# iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterate_dictionary(some_list):
    for i in some_list:
        # print(i.keys(), i.values())
        print(f"first_name - {i['first_name']}, last_name - {i['last_name']} \n")

iterate_dictionary(students)

def iterateDictionary(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])

iterateDictionary('last_name', students)


# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_info(dict_0):
    for key, value in dict_0.items():
        print(len(value), key.upper())
        for i in value:
            print(i)
print_info(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
