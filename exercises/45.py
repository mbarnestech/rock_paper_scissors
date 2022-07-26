'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

def last_element(list1):
    if len(list1)==0:
        return None      
    return list1.pop()

print(last_element([5,4,2]))
print(last_element([]))

# Demo answer
# def last_element(l):
#     if l:               # my note - works because empty lists are falsy
#         return l[-1]    # same function in this case as my use of pop, but pop would change the list element where this doesn't.
#     return None