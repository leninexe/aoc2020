# Read Input
f = open("input.txt", "r")

numbers = {}
splitter = f.readline().strip().split(",")

for i in range(len(splitter)):
	numbers[int(splitter[i])] = i + 1

mostRecent = int(splitter[len(splitter) - 1])
previousTurn = 0

for turn in range(1, 30000001):

	if turn <= len(splitter):
		continue

	if previousTurn == 0:
		mostRecent = 0
		previousTurn = numbers.get(mostRecent, 0)
		numbers[mostRecent] = turn
		continue

	mostRecent = numbers[mostRecent] - previousTurn
	previousTurn = numbers.get(mostRecent, 0)
	numbers[mostRecent] = turn

print(mostRecent)