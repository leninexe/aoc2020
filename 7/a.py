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

candidates = set(())
candidates.add("shiny gold")

currentSize = len(candidates)
oldSize = 0

while len(candidates) != oldSize:
	oldSize = len(candidates)

	for bl in bagLogic:
		newCandidates = set(())

		for c in candidates:
			if list(bagLogic[bl].keys()).count(c) > 0:
				newCandidates.add(bl)

		candidates.update(newCandidates)

candidates.remove("shiny gold")
print(len(candidates))