class Node:
	def __init__(self, value, operation):
		self.value = value
		self.operation = operation
		self.childs = []

def buildTree(expression):
	i = 0
	previousNode = None

	while i < len(expression):
		c = expression[i]

		if c == "(":
			start = i + 1
			length = findClosingParantheses(expression[start:])

			# print("Start: " + str(start) + ", Length: " + str(length) + ", SubExpression: " + expression[start:start + length])

			parenthesesNode = buildTree(expression[start:start + length])

			if previousNode != None:
				previousNode.childs.append(parenthesesNode)
			else:
				previousNode = parenthesesNode

			i += length
		elif c == ")":
			pass
		elif c == "+" or c == "*":
			operationNode = Node(None, c)
			operationNode.childs.append(previousNode)
			previousNode = operationNode
		else:
			#c is a value
			valueNode = Node(int(c), None)

			if previousNode != None:
				previousNode.childs.append(valueNode)
			else:
				previousNode = valueNode

		i += 1

	return previousNode

def findClosingParantheses(subExpression):
	depth = 1

	for i in range(len(subExpression)):
		c = subExpression[i]

		if c == "(": depth += 1
		elif c == ")": depth -= 1

		if depth == 0:
			return i

def printTree(root):
	if len(root.childs) == 0:
		if root.value != None:
			print("ValueNode: " + str(root.value))
		else:
			print("OperationNode: " + root.operation)
	else:	
		print("OperationNode: " + root.operation)

		for c in root.childs:
			printTree(c)

def evaluateTree(root):
	if len(root.childs) == 0:
		return root.value
	else:
		if root.operation == "*":
			return evaluateTree(root.childs[0]) * evaluateTree(root.childs[1])
		elif root.operation == "+":
			return evaluateTree(root.childs[0]) + evaluateTree(root.childs[1])

# Read Input
f = open("input.txt", "r")

expressions = []

for line in f:
	expressions.append(line.strip().replace(" ",""))

sumOfExpressions = 0

for expression in expressions:
	# print(expression)

	# tree = buildTree(expression)
	# printTree(tree)
	# print(evaluateTree(tree))

	sumOfExpressions += evaluateTree(buildTree(expression))

print(sumOfExpressions)



