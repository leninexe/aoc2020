# Read Input
f = open("input.txt", "r")

adapters = []

oneJoltDifference = 0
threeJoltDifference = 1
joltageRating = 0

for line in f:
	adapters.append(int(line.strip()))

adapters.sort()

for i in adapters:
	if i - 1 == joltageRating:
		oneJoltDifference += 1
	elif i - 3 == joltageRating:
		threeJoltDifference += 1

	joltageRating = i

print(oneJoltDifference * threeJoltDifference)