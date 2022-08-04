def extract_full_name(nameset):
	# return list(map(lambda x: (x.get("first") + " " + x.get("last")), nameset))
	return list(map(lambda x: (x["first"] + " " + x["last"]), nameset))

names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names)) # ['Elie Schoppik', 'Colt Steele']