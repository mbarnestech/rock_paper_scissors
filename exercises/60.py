# Not using **kwargs
# def calculate(make_float, operation, first, second, message="The result is") :
#         if operation == "add" :
#             result = first + second
#         elif operation == "subtract" :
#             result = first - second
#         elif operation == "multiply" :
#             result = first * second
#         else:
#             result = first / second
#         if not make_float:
#             result = int(result)
#         else:
#             result = float(result)
#         return "{} {}".format(message, result)


# using **kwargs

def calculate(**kwargs) :
    if kwargs['operation'] == "add" :
            result = kwargs['first'] + kwargs['second']
    elif kwargs['operation'] == "subtract" :
        result = kwargs['first'] - kwargs['second']
    elif kwargs['operation'] == "multiply" :
        result = kwargs['first'] * kwargs['second']
    else:
        result = kwargs['first'] / kwargs['second']
    if not kwargs['make_float'] :
        result = int(result)
    else:
        result = float(result)
    # if 'message' in kwargs:
    #     return "{} {}".format(kwargs['message'], result)
    # return "The result is {}".format(result)
    return "{} {}".format(kwargs.get('message', 'The result is'), result) # hadn't thought to use .get(); tried after checking solution

print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4)) # "You just added 6"
print(calculate(make_float=True, operation='divide', first=3.5, second=5)) # "The result is 0.7"