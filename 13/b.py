def extended_gcd(a, b):
	old_r, r = a, b
	old_s, s = 1, 0
	old_t, t = 0, 1

	while r:
		quotient, remainder = divmod(old_r, r)
		old_r, r = r, remainder
		old_s, s = s, old_s - quotient * s
		old_t, t = t, old_t - quotient * t

	return old_r, old_s, old_t

def combine_phased_rotations(a_period, a_phase, b_period, b_phase):
	gcd, s, t = extended_gcd(a_period, b_period)
	phase_difference = a_phase - b_phase
	pd_mult, pd_remainder = divmod(phase_difference, gcd)

	if pd_remainder:
		raise ValueError("Rotation reference points never synchronize.")

	combined_period = a_period // gcd * b_period
	combined_phase = (a_phase - s * pd_mult * a_period) % combined_period

	return combined_period, combined_phase

def arrow_alignment(red_len, green_len, advantage):
	period, phase = combine_phased_rotations(red_len, 0, green_len, -advantage % green_len)

	return -phase % period

def gcd(a, b):
	remainder = 0
	stopper = False

	while not stopper:
		remainder = a % b
		a = b
		b = remainder
		stopper = b == 0

	return a

def lcm(a, b):
	return (a * b) / gcd(a, b)

# Read Input
f = open("input.txt", "r")

f.readline()
busNotes = f.readline().strip().split(",")
times = {}

for i in range(len(busNotes)):
	if busNotes[i] != "x":
		times[i] = int(busNotes[i])

nextMatch = arrow_alignment(times[list(times.keys())[0]], times[list(times.keys())[1]], list(times.keys())[0] - list(times.keys())[1])
step = lcm(times[list(times.keys())[0]], times[list(times.keys())[1]])

for i in range(2, len(times)):
	offset = list(times.keys())[i]
	value = times[offset]

	while not (nextMatch + offset) % value == 0:
		nextMatch += step

	step = lcm(step, value)

print(int(nextMatch))

