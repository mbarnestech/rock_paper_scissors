def contains_purple(*args):
	if "purple" in args:
		return True
	return False


print(contains_purple(False, "purple", "blue", 3))
print(contains_purple(True))