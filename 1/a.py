# Read Input
f = open("input.txt", "r")

numbers = []

for l in f:
	numbers.append(int(l.strip()))

result = None

for n1 in numbers:
	for n2 in numbers:
		if n1 + n2 == 2020:
			result = n1 * n2

		if result != None:
			break

	if result != None:
		break

print(result)