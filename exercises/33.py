person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer

# take 1

answer = {person[x][0]:person[x][1] for x in range(0, len(person))}
print(answer)

# take 2

answer2 = {item[0]:item[1] for item in person}
print(answer2)

# take 3

answer3 = dict(person)
print(answer3)

# take 4

answer4 = {x:y for x,y in person}
print(answer4)