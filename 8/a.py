# Read Input
f = open("input.txt", "r")

ACC = "acc"
JMP = "jmp"
NOP = "nop"

pc = 0
accumulator = 0
commands = []

for line in f:
	splitter = line.strip().split(" ")
	cmd = splitter[0]
	arg = int(splitter[1])
	commands.append({"cmd": cmd, "arg": arg})

visited = []

while pc >= 0 and pc < len(commands):
	if visited.count(pc) > 0:
		break

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