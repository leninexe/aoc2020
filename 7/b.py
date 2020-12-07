def sumContainedBags(rules, color, amount):
	amountOfBags = amount

	for v in rules[color]:
		amountOfBags += sumContainedBags(rules, v, amount * rules[color][v])

	return amountOfBags

# Read Input
f = open("input.txt", "r")

bagLogic = {}

for line in f:
	parts = line.strip().split("contain")
	outer = parts[0].replace("bags", "").strip()
	innerParts = parts[1].strip().split(",")

	contents = {}

	for i in range(len(innerParts)):
		inner = innerParts[i].strip().replace("bags", "").replace("bag", "").replace(".", "").strip()

		if inner != "no other":
			amount = inner.split(" ", 1)[0]
			color = inner.split(" ", 1)[1]

			contents[color] = int(amount)

	bagLogic[outer] = contents

print(sumContainedBags(bagLogic, "shiny gold", 1) - 1)
