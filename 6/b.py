# Read Input
f = open("input.txt", "r")

currentSet = None
sets = []

for line in f:
	if line.strip() == "":
		sets.append(currentSet)

		currentSet = None
	else:
		if currentSet == None:
			currentSet = set(())

			for c in line.strip():
				currentSet.add(c)
		else:
			newSet = set(())

			for c in line.strip():
				newSet.add(c)

			currentSet.intersection_update(newSet)

sets.append(currentSet)

sumQuestions = 0

for s in sets:
	sumQuestions += len(s)

print(sumQuestions)