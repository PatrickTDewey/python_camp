def multiply(num_list, num):
    multiplied = []
    for x in num_list:
        print(x)
        multiplied.append(x*num)
        print(x)
    return multiplied
a = [2,4,10,16]
b = multiply(a,5)
print(b)

def other_way_multiply(num_list, factor):
    for x in range(len(num_list)):
        print(num_list[x])
        num_list[x] *= factor
    return num_list
print(other_way_multiply(a, 2))