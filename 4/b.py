import re

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
validEyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

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

	if valid:
		valid &= int(p[birthYear]) >= 1920 and int(p[birthYear]) <= 2002
		valid &= int(p[issueYear]) >= 2010 and int(p[issueYear]) <= 2020
		valid &= int(p[expirationYear]) >= 2020 and int(p[expirationYear]) <= 2030

		if re.search("^[0-9]+cm\Z", p[height]) != None or re.search("^[0-9]+in\Z", p[height]) != None:
			h = int(re.findall("[0-9]+", p[height])[0])
			unit = p[height][-2:]
			valid &= (unit == "cm" and h >= 150 and h <= 193) or (unit == "in" and h >= 59 and h <= 76)
		else:
			valid = False

		valid &= re.search("^#[0-9a-fA-F]{6}\Z", p[hairColor]) != None
		valid &= validEyeColors.count(p[eyeColor]) == 1		
		valid &= re.search("^[0-9]{9}\Z", p[passportId]) != None

	if valid: validPassports += 1

print(validPassports)