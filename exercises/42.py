# def speak(animal="dog"):
# 	if animal=="pig":
# 		return "oink"
# 	elif animal=="duck":
# 		return "quack"
# 	elif animal=="dog":
# 		return "woof"
# 	elif animal=="cat":
# 		return "meow"
# 	else:
# 		return "?"

# dictionary solution
def speak(animal="dog"):
    noises = {"pig":"oink", "duck":"quack", "cat":"meow", "dog":"woof"}
    if animal in noises:
    	return noises.get(animal)
    return "?"

#testing Todd's solution
# def speak(animal='dog'):
#     noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
#     return noises.get(animal, '?')

print(speak("pig"))
print(speak())
print(speak("ostrich"))