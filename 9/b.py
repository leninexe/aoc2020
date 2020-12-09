# Read Input
f = open("input.txt", "r")

numbers = []

for line in f:
	numbers.append(int(line.strip()))

preambleLength = 25
invalidNumber = None
maxIndex = None

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
		maxIndex = i
		invalidNumber = numbers[i]
		break

first = None
last = None

for i in range(0, maxIndex):
	numberSum = 0

	for j in range(i, maxIndex):
		numberSum += numbers[j]

		if numberSum > invalidNumber: break

		if numberSum == invalidNumber:
			first = i
			last = j
			break

	if first != None and last != None: break

sumNumbers = numbers[first:last + 1]
minNumber = None
maxNumber = None

for n in numbers[first:last + 1]:
	if minNumber == None or n < minNumber:
		minNumber = n

	if maxNumber == None or n > maxNumber:
		maxNumber = n

print(minNumber + maxNumber)