import re

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
currentRegex = rules[0][0]
print(currentRegex)

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

print(currentRegex)

print(buildRegexFromList(currentRegex))
currentRegex = "^" + buildRegexFromList(currentRegex) + "$"
print(currentRegex)

validCount = 0

for m in messages:
 	if re.search(currentRegex, m) != None: validCount += 1

print(validCount)