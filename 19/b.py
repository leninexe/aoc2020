import re

def prepareRegex(rules, ruleId):
	currentRegex = rules[ruleId]

	replacementsDone = True

	while replacementsDone:
		replacementsDone = False
		newRegex = []

		for r in currentRegex:
			if type(r) == str:
				newRegex.append(r)
			else:
				newRegex.append(getSubReplacements(rules, r))

		replacementsDone = newRegex != currentRegex
		currentRegex = newRegex

	return currentRegex

def getSubReplacements(rules, ruleIds):
	if type(ruleIds) == int:
		return rules[ruleIds]
	elif type(ruleIds) == list:
		newReplacements = []

		for ruleId in ruleIds:
			if ruleId == "|":
				newReplacements.append("|")
			else:
				newReplacements.append(getSubReplacements(rules, ruleId))

		return newReplacements
	return ruleIds

def buildRegexFromList(items):
	result = ""

	if type(items) == list:
		if len(items) > 1:
			result += "("

			for i in items:
				if type(i) == str:
					result += i
				else:
					result += buildRegexFromList(i)

			result += ")"
		else:
			result += buildRegexFromList(items[0])
	else:
		result += items

	return result

# Read Input
f = open("input.txt", "r")

lastRuleRead = False

rules = {}
messages = []
history = {}

for line in f:
	if line.strip() == "":
		lastRuleRead = True

	if not lastRuleRead:
		#Read rule
		splitter = line.strip().split(":")
		number = int(splitter[0].strip())
		rule = splitter[1].strip()

		if rule[0] == "\"":
			rules[number] = rule[1:len(rule) - 1]
		else:
			splitter = rule.split("|")
			alternatives = []

			for spl in splitter:
				ruleSequence = []
				sequence = spl.strip().split(" ")

				for subRule in sequence:
					ruleSequence.append(int(subRule.strip()))

				alternatives.append(ruleSequence)
				alternatives.append("|")

			alternatives = alternatives[:-1]
			rules[number] = alternatives
	else:
		messages.append(line.strip())

print(rules)

# Build Regex!
regexFor0 = buildRegexFromList(prepareRegex(rules, 0))
regexFor8 = "^" + buildRegexFromList(prepareRegex(rules, 8))
regexFor11 = "^" + buildRegexFromList(prepareRegex(rules, 11))
regexFor42 = "^" + buildRegexFromList(prepareRegex(rules, 42))
regexFor31 = "^" + buildRegexFromList(prepareRegex(rules, 31))

validCount = 0

for m in messages:
	nextMatch = re.search(regexFor42, m)
	offset = 0
	count42 = 0
	count31 = 0

	while nextMatch != None:
		count42 += 1
		offset += nextMatch.span()[1]
		nextMatch = re.search(regexFor42, m[offset:]) 

	nextMatch = re.search(regexFor31, m[offset:])

	while nextMatch != None:
		count31 += 1
		offset += nextMatch.span()[1]
		nextMatch = re.search(regexFor31, m[offset:])

	if count42 > count31 and count31 > 0 and offset == len(m): validCount += 1

	# start8 = re.search(regexFor8, m)

	# if start8 != None:
	# 	offset = start8.span()[1]

	# 	count42 = 0
	# 	nextMatch = start8

	# 	while nextMatch != None:
	# 		nextMatch = re.search(regexFor42, m[offset:])

	# 		if nextMatch != None:
	# 			count42 += 1
	# 			offset += nextMatch.span()[1]

	# 	count31 = 0
	# 	nextMatch = True

	# 	while nextMatch != None:
	# 		nextMatch = re.search(regexFor31, m[offset:])

	# 		if nextMatch != None:
	# 			count31 += 1
	# 			offset += nextMatch.span()[1]

	# 	print(count42)
	# 	print(count31)

print(validCount)