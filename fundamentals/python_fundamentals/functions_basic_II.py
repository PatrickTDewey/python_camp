def countdown(x):
    new_list = []
    for x in range(x, -1, -1):
        new_list.append(x)
    return new_list
print(countdown(5))


def print_and_return(a, b):
    print(a)
    return b
print(print_and_return(3, 5))


def first_plus_length(li):
    sum = 0
    sum += li[0] + len(li)
    return sum

print(first_plus_length([1,2,3,4,5]))


def greater_than_second(li):
    count = 0
    new_list = []
    if len(li) < 2:
        return False
    else:
        for x in range(len(li)):
            if li[x] > li[1]:
                new_list.append(li[x])
                count += 1
        return (count, new_list)

print(greater_than_second([5,2,3,2,1,4]))
print(greater_than_second([3]))

def this_len_that_val(len, val):
    new_list = []
    for x in range(len):
        new_list.append(val)
    return new_list
print(this_len_that_val(4, 7))
