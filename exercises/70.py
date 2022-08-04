def triple_and_filter(nums):
	return [3*x for x in nums if x % 4 == 0]
	




print(triple_and_filter([1,2,3,4])) # [12]
print(triple_and_filter([6,8,10,12])) # [24,36]