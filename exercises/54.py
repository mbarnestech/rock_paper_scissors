def compact(values):

	# My initial solution:

	# values = [0,1,2,"",[], False, {}, None, "All done"]
	# new = [values[bool(i)==True] for i in values]

	# values2 = []
	# values3 = []
	# for i in new:
	# 	if i==1:
	# 		values2.append(values.pop(0))
	# 	else:
	# 		values3.append(values.pop(0))	
	# return values2
	
	# print(new)
	# print(values)
	# print(values2)
	# print(values3)

	# Simpler solution - I had tried this but with val==True at the end, which doesn't work. This solidified for me that 'if variable' includes the ==True and adding that check again isn't just redundant, it's asking the program to do something entirely different.

	return [val for val in values if val] 

print(compact([0,1,2,"",[], False, {}, None, "All done"])) # [1,2, "All done"]

