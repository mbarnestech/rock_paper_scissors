def extremes(content):
	return (min(content), max(content))

print(extremes([1,2,3,4,5]))  # (1, 5)

print(extremes((99,25,30,-7)))  # (-7, 99)

print(extremes("alcatraz"))  #( 'a', 'z')

