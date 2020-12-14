class Node:
	def __init__(self, value):
		self.value = value
		self.childs = []

	def appendChild(self, child):
		self.childs.append(child)

def buildTree(value):
	node = Node(value[0])
	
	if len(value) > 1:
		if value[1] == "X":
			node.appendChild(buildTree("0" + value[2:]))
			node.appendChild(buildTree("1" + value[2:]))
		else:
			node.appendChild(buildTree(value[1] + value[2:]))

	return node

def getPossibleValues(prefix, node):
	result = []

	if len(node.childs) == 0:
		result.append(int(prefix + node.value, 2))
	else:
		for c in node.childs:
			childResults = getPossibleValues(prefix + node.value, c)

			for cr in childResults:
				result.append(cr)

	return result

def maskValue(mask, value):
	binary = format(value, "b").zfill(36)
	result = []

	for i in range(len(mask)):
		if mask[i] != "0":
			result.append(mask[i])
		else: 
			result.append(binary[i])

	return "".join(result)

# Read Input
f = open("input.txt", "r")
memory = {}
mask = "X" * 36

for line in f:
	parts = line.strip().split("=")

	if parts[0].strip() == "mask":
		mask = parts[1].strip()
	else:
		memoryBank = maskValue(mask, int(parts[0].split("[")[1].split("]")[0]))
		value = int(parts[1].strip())

		floating = {}

		if memoryBank.find("X") > -1:
			root = buildTree("0" + memoryBank)

			for mb in getPossibleValues("", root):
				memory[mb] = value
		else:
			memory[int(memoryBank, 2)] = value

sum = 0

for v in memory.values():
	sum += v

print(sum)