nums = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
set_nums = {num for num in nums}
list_nums = [num for num in nums]
print(set_nums)
print(list_nums)

print(nums)
squared_evens = {num if num %2 != 0 else num*num for num in nums}
print(squared_evens)