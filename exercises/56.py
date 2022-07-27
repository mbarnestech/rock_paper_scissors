def partition(nums, callback):
    return [[val for val in nums if callback(val)], [val for val in nums if not callback(val)]]





def isEven(num):
    return num % 2 == 0

print(partition([1,2,3,4], isEven)) # [[2,4],[1,3]]