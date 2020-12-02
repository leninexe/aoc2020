# Read Input
f = open("input.txt", "r")

validPasswords = 0

for l in f:
	rule = l.strip().split(' ')
	firstIndex = int(rule[0].split('-')[0])
	secondIndex = int(rule[0].split('-')[1])
	letter = rule[1][:-1]
	password = rule[2]

	if password[firstIndex - 1] == letter and password[secondIndex - 1] != letter or password[firstIndex - 1] != letter and password[secondIndex - 1] == letter:
		validPasswords += 1

print(validPasswords)