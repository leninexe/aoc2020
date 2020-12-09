# Read Input
f = open("input.txt", "r")

numbers = []

for line in f:
	numbers.append(int(line.strip()))

preambleLength = 25

for i in range(preambleLength + 1, len(numbers)):
	preamble = numbers[i - preambleLength:i]
	valid = False

	for x in range(0, len(preamble) - 1):
		for y in range(1, len(preamble)):
			if x != y and preamble[x] + preamble[y] == numbers[i]:
				valid = True

			if valid: break

		if valid: break

	if not valid:
		print(numbers[i])
		break