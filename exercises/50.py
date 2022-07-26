def is_palindrome(possible_palindrome):
    clean_entry = possible_palindrome.lower().replace(" ", "")

    # Original code, overly long. Can simply ask for a return on the == statement and it will give True or False

    # if clean_entry == clean_entry[::-1]:
    #     return True
    # return False

    return clean_entry == clean_entry[::-1]

print(is_palindrome("testing THis with spaces and CASES "))
print(is_palindrome('testing')) # False
print(is_palindrome('tacocat')) # True
print(is_palindrome('hannah')) # True
print(is_palindrome('robert')) # False
print(is_palindrome('amanaplanacanalpanama'))  # True