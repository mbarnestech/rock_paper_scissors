# Creating decrement list without using 'def', just mapping and nested lambdas
decrement_list = lambda num: list(map(lambda x: x-1, num))


print(decrement_list([1,2,3]))
print(decrement_list([20,14,11]))

# Creating decrement list with 'def' and mapping.
def decrement_list2(numlist):
	return list(map(lambda x: x-1, numlist))

print(decrement_list2([1,2,3,2]))
print(decrement_list2([20,14,11,2]))
