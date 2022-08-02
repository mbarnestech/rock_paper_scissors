def remove_negatives(nums):
    return list(filter(lambda x: x>=0, nums))


print(remove_negatives([-1,3,4,-99]))
print(remove_negatives([-7,0,1,2,3,4,5]))
print(remove_negatives([50,60,70]))

