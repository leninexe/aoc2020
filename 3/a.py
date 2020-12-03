# Read Input
f = open("input.txt", "r")

rows = []

for l in f:
	row = []

	for c in l.strip():
		row.append(c)

	rows.append(row)

horizontal = 3
vertical = 1

x = 0
y = 0
encounteredTrees = 0

while y < len(rows):
	if rows[y][x] == '#':
		encounteredTrees += 1

	x += horizontal
	x = x % len(rows[0])
	y += vertical

print(encounteredTrees)