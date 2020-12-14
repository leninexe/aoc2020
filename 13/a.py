# Read Input
f = open("input.txt", "r")

earliestTimestamp = int(f.readline().strip())
busNotes = f.readline().strip()
busIds = []

for busLine in busNotes.split(","):
	if busLine != "x":
		busIds.append(int(busLine))

busIds.sort()

timestamp = earliestTimestamp
matchingBus = None

while matchingBus == None:
	for bus in busIds:
		if timestamp % bus == 0:
			matchingBus = bus
			break

	if matchingBus == None:	timestamp += 1

print(matchingBus * (timestamp - earliestTimestamp))