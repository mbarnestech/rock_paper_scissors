def sum_floats(*args):
    return sum(x for x in args if type(x) == float)


print(sum_floats(1.5, 2.4, 'awesome', [], 1)) # 3.9
print(sum_floats(1,2,3,4,5)) # 0