def combine_words(solo_word, **kwargs):
	if "suffix" in kwargs:
		return solo_word + kwargs["suffix"]
	elif "prefix" in kwargs:
		return kwargs["prefix"] + solo_word
	return solo_word

print(combine_words("child", suffix="ish"))
print(combine_words("child", prefix="man"))
print(combine_words("child", prefix="man", suffix="ish"))
print(combine_words("child", suffix="ish", prefix="man"))
print(combine_words("child"))