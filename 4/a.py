# Read Input
f = open("input.txt", "r")

birthYear = "byr"
issueYear = "iyr"
expirationYear = "eyr"
height = "hgt"
hairColor = "hcl"
eyeColor = "ecl"
passportId = "pid"
countryId = "cid"

requiredFields = [birthYear, issueYear, expirationYear, height, hairColor, eyeColor, passportId]

idx = 0
passports = []
passports.append({})

for l in f:
	if l.strip() == "":
		passports.append({})
		idx += 1
	else:
		fields = l.strip().split(" ")

		for f in fields:
			passports[idx][f.split(":")[0]] = f.split(":")[1]

validPassports = 0

for p in passports:
	valid = True

	for rf in requiredFields:
		valid &= list(p.keys()).count(rf) > 0

	if valid: validPassports += 1

print(validPassports)