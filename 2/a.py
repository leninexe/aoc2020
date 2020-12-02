# Read Input
f = open("input.txt", "r")

validPasswords = 0

for l in f:
	rule = l.strip().split(' ')
	minOccurences = int(rule[0].split('-')[0])
	maxOccurences = int(rule[0].split('-')[1])
	letter = rule[1][:-1]
	password = rule[2]

	count = 0

	for c in password:
		if c == letter:
			count += 1

	if count >= minOccurences and count <= maxOccurences:
		validPasswords += 1

print(validPasswords)