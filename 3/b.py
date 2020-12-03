# Read Input
f = open("input.txt", "r")

rows = []

for l in f:
	row = []

	for c in l.strip():
		row.append(c)

	rows.append(row)

variants = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
variantEncounteredTrees = []

for variant in variants:
	horizontal = variant[0]
	vertical = variant[1]

	x = 0
	y = 0
	encounteredTrees = 0

	while y < len(rows):
		if rows[y][x] == '#':
			encounteredTrees += 1

		x += horizontal
		x = x % len(rows[0])
		y += vertical

	variantEncounteredTrees.append(encounteredTrees)

result = 1

for et in variantEncounteredTrees:
	result *= et

print(result)