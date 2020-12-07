# Read Input
f = open("input.txt", "r")

currentSet = set(())
sets = []

for line in f:
	if line.strip() == "":
		sets.append(currentSet)

		currentSet = set(())
	else:
		for c in line.strip():
			currentSet.add(c)

sets.append(currentSet)

sumQuestions = 0

for s in sets:
	sumQuestions += len(s)

print(sumQuestions)