def multiple_letter_count(string):
	letters = list(set(string)) # ends up changing order of letters in word by switching it to a set then back to a list
	return {letters[num]:string.count(letters[num]) for num in range(0,len(letters))}


print(multiple_letter_count("falafels"))

# glanced at solution - I of course made things way harder than they needed to be.

def multiple_letter_count(string):
	return {num: string.count(num) for num in string} # letters stay in same order; need to look up more on dictionaries. disregards all non-unique keys?	

print(multiple_letter_count("falafels"))