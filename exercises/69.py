# Write a function interleave  that accepts two strings.  It should return a new string containing the 2 strings interwoven or zipped together. 

# My first attempt:

def interleave(first, second):
    newlist = list(zip(first, second))
    final = ''
    for first_tuple, second_tuple in newlist:
        final += first_tuple
        final += second_tuple
    return final

print(interleave('hi','ha'))    # 'hhia'

print(interleave('aaa', 'zzz'))  # 'azazaz'

print(interleave('lzr','iad')) #  'lizard'

# After seeing solution uses .join & list comprehension, trying again for a more concise solution:

def interleave2(first, second):
    #return ''.join(''.join(x) for x in zip(first,second))
    return ''.join(x+y for x,y in zip(first,second)) # I like this but I think the line above is more versatile

print(interleave2('hi','ha'))    # 'hhia'

print(interleave2('aaa', 'zzz'))  # 'azazaz'

print(interleave2('lzr','iad')) #  'lizard'
