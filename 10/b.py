class Node:
	def __init__(self, value):
		self.value = value
		self.childs = []

	def appendChild(self, child):
		self.childs.append(child)

def createTree(joltage, adapters, index):
	node = Node(adapters[index])

	for i in range(1, 4):
		if index + i < len(adapters) and adapters[index + i] - node.value <= 3:
			node.childs.append(createTree(node.value, adapters, index + i))

	return node

def countLeafs(node):
	numLeafs = 0

	if len(node.childs) == 0:
		return 1
	else:
		for c in node.childs:
			numLeafs += countLeafs(c)

		return numLeafs

# Read Input
f = open("input.txt", "r")

adapters = [0]

joltageRating = 0

for line in f:
	adapters.append(int(line.strip()))

adapters.sort()
adapters.append(adapters[len(adapters) - 1] + 3)

groups = []
lastGroupIndex = 0

#Split adapters on 3jolts
for i in range(len(adapters) - 1):
	if adapters[i] + 3 == adapters[i + 1]:
		groups.append(adapters[lastGroupIndex:i + 1])
		lastGroupIndex = i + 1

numLeafs = 1

for grp in groups:
	if len(grp) > 2:
		groupTree = createTree(grp[0], grp, 0)
		numLeafs *= countLeafs(groupTree)

print(numLeafs)