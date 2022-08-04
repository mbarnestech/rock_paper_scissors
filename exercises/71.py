def extract_full_name(nameset):
	# First Try:
	# return list(map(lambda x: (x.get("first") + " " + x.get("last")), nameset))
	#After checking solution, turns out the .get() was unecessary - this is a little shorter:
	return list(map(lambda x: (x["first"] + " " + x["last"]), nameset))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']