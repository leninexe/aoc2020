def maskValue(mask, value):
	binary = format(value, "b").zfill(36)
	result = []

	for i in range(len(mask)):
		if mask[i] != "X":
			result.append(mask[i])
		else:
			result.append(binary[i])

	return int("".join(result), 2)

# Read Input
f = open("input.txt", "r")
memory = {}
mask = "X" * 36

for line in f:
	parts = line.strip().split("=")

	if parts[0].strip() == "mask":
		mask = parts[1].strip()
	else:
		memoryBank = int(parts[0].split("[")[1].split("]")[0])
		value = maskValue(mask, int(parts[1].strip()))
		memory[memoryBank] = value


sum = 0

for v in memory.values():
	sum += v

print(sum)