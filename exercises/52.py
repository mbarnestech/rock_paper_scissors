def multiply_even_numbers(list_of_numbers):
    total = 1
    for x in list_of_numbers:
        if x%2==0:
            total *= x
    return total


print(multiply_even_numbers([2,3,4,5,6])) # 48