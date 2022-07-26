#define single_letter_count below:

# def single_letter_count(word, letter):
# 	count = 0
# 	for char in word.upper():
# 		if char == letter.upper():
# 			count += 1
# 	return count

# print(single_letter_count("Hello World", "h")) # 1
# print(single_letter_count("Hello World", "z")) # 0
# print(single_letter_count("HelLo World", "l")) # 3

# looked at answer; seeing if I can rework my solution from memory...

def single_letter_count(word, letter):
	return word.upper().count(letter.upper())

print(single_letter_count("Hello World", "h")) # 1
print(single_letter_count("Hello World", "z")) # 0
print(single_letter_count("HelLo World", "l")) # 3