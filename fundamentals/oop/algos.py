def one_to_255():
    for i in range(1, 256):
        print(i)
print(one_to_255())

def find_and_print_max(nums):
    max = nums[0]
    for num in range(1, len(nums)):
        print(nums[num])
        if nums[num] > max:
            max = nums[num]
    return max
print(find_and_print_max([1,2,3,4,5,6,2]))