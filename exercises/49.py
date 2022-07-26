def list_manipulation(list1, command, location, value=0):
	if command == "remove":
		if location == "end":
			return list1.pop()
		return list1.pop(0)
	else:
		if location == "end":
			return list1 + [value] # originally tried using .append(); learned I can't use on return line
		return [value] + list1 # same as above comment but with .insert()


print(list_manipulation([1,2,3], "remove", "end")) # 3
print(list_manipulation([1,2,3], "remove", "beginning")) #  1
print(list_manipulation([1,2,3], "add", "beginning", 20)) #  [20,1,2,3]
print(list_manipulation([1,2,3], "add", "end", 30)) #  [1,2,3,30]