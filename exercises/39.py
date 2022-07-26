#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)

def generate_evens():
	return [x for x in range(2,50,2)]

print(generate_evens())