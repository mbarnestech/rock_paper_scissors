# Write a function max_magnitude  that accepts a single list full of numbers. It should return the magnitude of the number with the largest magnitude (the number that is furthest away from zero).



def max_magnitude(nums):
	return max((abs(x)) for x in nums)

print(max_magnitude([300, 20, -900]))   #900

print(max_magnitude([10, 11, 12]))   #12

print(max_magnitude([-5, -1, -89]))   #89