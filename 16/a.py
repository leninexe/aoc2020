# Read Input
f = open("input.txt", "r")

RULES = 0
MYTICKET = 1
NEARBYTICKETS = 2

rules = {}
allRuleValues = []
myTicket = []
nearbyTickets = []

state = RULES

for line in f:
	if line.strip() == "":
		continue

	if line.strip() == "your ticket:":
		state = MYTICKET
		continue
	elif line.strip() == "nearby tickets:":
		state = NEARBYTICKETS
		continue

	if state == RULES:
		splitter = line.split(":")
		pairs = splitter[1].split("or")
		values = []

		for pair in pairs:
			minValue = int(pair.strip().split("-")[0])
			maxValue = int(pair.strip().split("-")[1])

			values.append([minValue, maxValue])
			allRuleValues.append([minValue, maxValue])

		rules[splitter[0].strip()] = values
	elif state == MYTICKET:
		for i in line.split(","):
			myTicket.append(int(i.strip()))
	elif state == NEARBYTICKETS:
		ticket = []

		for i in line.split(","):
			ticket.append(int(i.strip()))

		nearbyTickets.append(ticket)

sumInvalid = 0

for ticket in nearbyTickets:
	for number in ticket:
		valid = False

		for ruleValues in allRuleValues:
			if number >= ruleValues[0] and number <= ruleValues[1]:
				valid = True
				break

		if not valid: sumInvalid += number

print(sumInvalid)