import copy

def detectLoop(commands):
	pc = 0
	accumulator = 0
	visited = []

	while pc >= 0 and pc < len(commands):
		if visited.count(pc) > 0:
			return True

		visited.append(pc)

		cmd = commands[pc]["cmd"]
		arg = commands[pc]["arg"]

		if cmd == NOP:
			pc += 1
		elif cmd == ACC:
			accumulator += arg
			pc += 1
		elif cmd == JMP:
			pc += arg

	print(accumulator)
	return False

# Read Input
f = open("input.txt", "r")

ACC = "acc"
JMP = "jmp"
NOP = "nop"

pc = 0
accumulator = 0
commands = []
jmpIndices = []
nopIndices = []

for line in f:
	splitter = line.strip().split(" ")
	cmd = splitter[0]
	arg = int(splitter[1])
	commands.append({"cmd": cmd, "arg": arg})

	if cmd == JMP:
		jmpIndices.append(len(commands) - 1)
	elif cmd == NOP:
		nopIndices.append(len(commands) - 1)

for i in range(len(jmpIndices)):
	editedCommands = copy.deepcopy(commands)
	editedCommands[jmpIndices[i]]["cmd"] = NOP

	if not detectLoop(editedCommands):
		break

for i in range(len(nopIndices)):
	editedCommands = copy.deepcopy(commands)
	editedCommands[jmpIndices[i]]["cmd"] = JMP

	if not detectLoop(editedCommands):
		break