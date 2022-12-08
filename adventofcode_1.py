#! /bin/env python3


def getInput(filepath):
		with open(filepath, "r") as f:
			return f.read()

### DAY 7

def a7():
	data = getInput("input7.txt").split('\n')
	
	def makeTree(data):
		tree = dict({"/":{}})
		current = tree
		lineno = 0
		parents = []
		for d in data:
			print("lineno: ", lineno)
			lineno += 1
			parts = d.split(' ')
			if parts[0] == "$": # command
				if parts[1] == "cd": # go into directory
					print(parts)
					if parts[2] == "..":
						current = parents.pop()
					else:
						print("moving to " + parts[2])
						parents.append(current)
						current = current[parts[2]]

				elif parts[1] == "ls": # add subtrees / files
					pass
			else: # add subtrees / files
				print(parts)
				if parts[0] == "dir": # new subtree, empty
					current[parts[1]] = {}
				else:

					current[parts[1]] = int(parts[0])
		# print(tree)
		return tree
	

	t = makeTree(data)

	def addUp(tree, lst):
		summ = 0
		for i in tree:
			if type(tree[i]) is dict:
				summ += addUp(tree[i], lst)
			else:
				summ += tree[i]
		if summ <= 100000:
			lst.append(summ)
		return summ

	l = []
	total = addUp(t, l)
	print("pt1", sum(l))

	def searchSmallest(diff, tree):
		smol = []
		for k in tree:
			if type(tree[k]) is dict:
				summ = addUp(tree[k], [])
				if summ >= diff: #candidate
					smol.append([k, summ])
				smol += searchSmallest(diff, tree[k])
		return smol
	print("pt2")
	sm = searchSmallest(-40000000 + total, t)
	sm.sort(key=lambda x : x[1])
	print(sm[0][1])
a7()


### DAY 6

def a6():
	data = getInput("input6.txt")
	def solve(offset):
		ticker = 0
		for u in range(0, len(data) - offset):
			if (len(set(data[u : u + offset]))) == offset:
				return ticker + offset
			ticker += 1
	print("pt1", solve(4))
	print("pt2", solve(14))

# a6()



### DAY 5

def a5():
	data = getInput("input5.txt").split("\n")
	crates, instructions = data[:9], data[10:]
	def inst(instruction):
		amount = int(instruction.split(" ")[1])
		src = int(instruction[-6])
		dst = int(instruction[-1])
		return amount, src, dst


	def build_stacks():
		stacks = []
		for j in range(1, 34, 4):
			topdown = [crates[ii][j] for ii in range(0, 8) if crates[ii][j] != ' ']
			topdown.reverse()
			print(topdown)
			stacks.append(topdown)
		return stacks


	def move(stacks, amount, src, dst):
		print("src", src)
		print("dst", dst)
		for i in range(0, amount):
			stacks[dst - 1].append(stacks[src - 1].pop())
		return stacks


	stacks = build_stacks()
	print(stacks)

	def pt1():
		for i in instructions:
			move(stacks, *inst(i))


	print("pt1", "".join([stacks[i][-1] for i in range(0, 9)]))


	def movem(stacks, amount, src, dst):
		print("#", amount, "from", src, "to", dst)
		m = min(amount, len(stacks[src - 1]))
		print("m", m)
		if m != 0:
			stacks[dst-1] += stacks[src - 1][-m:]
			del stacks[src - 1][-m:]
		printStacks()
		return stacks

	def printStacks():
		print("==stack==")
		for i, p in enumerate(stacks):
			print(p)
			print(i + 1, "".join(p))
		print()

	def pt2(stacks):
		printStacks()
		s = stacks
		for i in instructions:
			s = movem(s, *inst(i))
		return s

	p2 = pt2(stacks)

	print("pt2", "".join([p2[i][-1] if len(p2[i]) > 0 else " " for i in range(0, 9) ]))


# a5()


### DAY 4

def a4():
	data = getInput("input4.txt").split('\n')

	def withRanges(inputs):
		sections = []
		for line in inputs:
			cs = line.split(',')
			c1 = cs[0].split('-')
			c2 = cs[1].split('-')
			# print(c1, c2)
			sections.append((set(range(int(c1[0]), int(c1[1]) + 1)), set(range(int(c2[0]), int(c2[1]) + 1))))
		print(sections[0])
		s = sections[len(sections) - 1]
		print(int(s[0] > s[1] or s[0] < s[1]) )
		print(sum((int(s[0] > s[1] or s[0] < s[1]) for s in sections)))
	def asScalars(line):
		return [int(l) for k in line.split(',') for l in k.split('-')]
	
	def isContaining(left, right):
		return (left[0] <= right[0] and left[1] >= right[1]) or (left[0] >= right[0] and left[1] <= right[1])


	def overlapping(left, right):
		def toRanges(left, right):
			return range(left[0], left[1] + 1), range(right[0], right[1] + 1)
		def toSets(left, right):
			return set(left), set(right)

		l, r = toSets(*toRanges(left, right))
		return len(l & r) > 0

	summ = 0
	sumb = 0
	for line in data:
		s = asScalars(line)
		if isContaining(s[:2], s[2:]):
			summ += 1
		if overlapping(s[:2], s[2:]):
			sumb += 1
	print("pt1", summ)
	print("pt2", sumb)



# a4()


### DAY 3

def a3():
	data = getInput("input3.txt").split('\n')


	def dehexString(chrs):
		coeff = 96 if chrs.islower() else 38
		return int(bytes(chrs, "ansi").hex(), 16) - coeff
	def get_compartments(line):
		con = dehexString("a")
		return [dehexString(k) for k in line[:len(line)//2]], [dehexString(k) for k in line[len(line)//2:]]

	def get_prio_score(comp1, comp2):
		summ = set()
		for x in comp1:
			for y in comp2:
				if x == y:
					summ.add(x)
					print("found 1:", x)
		return summ

	#print("pt1", sum({get_prio_score(*get_compartments(line)) for line in data}))
	gen = (get_prio_score(i, j) for i,j in (get_compartments(line) for line in data))
	print("pt1", sum([ll for l in gen for ll in l]))

	pt2 = [set(line) for line in data]
	total = []
	for i in range(0, len(pt2), 3):
		total.append(*(pt2[i] & pt2[i+1] & pt2[i+2]))
	total = sum(dehexString(t) for t in total)
	print("pt2", total)

#a3()
#### DAY 2
def a2():

	"""
A 1 rock
B 2 paper
C 3 scissors
###
X lose
Y draw
Z win

A X
A Y
A Z
B X
B Y
B Z
C X
C Y
C Z
wins:
r-p => 1 2 => 0 1 ratio: 1 - 2 => -1
p-s => 2 3 => 1 2 ratio: 2 - 3 => -1
s-r => 3 1 => 2 0 ratio: 3 - 1 => 2
((r1 % 3) + 1) - r2 = 0
ties:
00 => 1 - 0 ratio: 0
11 => 2 - 1
22 => 3 - 2
losses:
12
23
31
(r1 + 1) % 3 - r2 % 3 = 

if ((r1 % 3) + 1 = r2 % 3) => win

(r1 - r0) % 3
iff round[1]
"""
	data = getInput("input2.txt").split('\n')

	def get_score(r1, r2):
		# 0 tie
		# 1 lose
		# 2 win
		s = r2 - r1 
		# 1 tie
		# 2 lose
		# 0 win
		s = (s + 1) % 3
		# 0 tie
		# -1 lose
		# 1 win
		s -= 1
		return (s * 3) + 3 + r2

	def get_parts(line):
		return [int(bytes(x[0], "utf-8").hex(), 16) - x[1] for x in ([line[0], 64], [line[2], 87])]


	## part 1
	print("pt 1", sum([get_score(*get_parts(r)) for r in data]))


	"""
	e = 1, l = 1 => (1, 3) / (0, 2) lose: -1 % 3 
	e = 3, l = 3 => (3, 1) / (2, 0) win: 
	"""
	def get_combo(e, l):
		return e, (((e-1) + (l - 2)) % 3) + 1

	test = getInput("input_2_test.txt").split('\n')

	def ftest(strr):
		d = dict({
			1: "rock",
			2: "paper",
			3: "scissors"
			})
		d1 = dict({
			1: "lose",
			2: "draw",
			3: "lose"
			})
		print("=====", strr, "=====")
		attacker, strat = get_parts(strr)
		print(f"we want to {d1[strat]} against {d[attacker]} so we choose {d[get_combo(attacker, strat)[1]]}")

	for t in test: 
		ftest(t)
	"""

	print(get_score(*get_combo(*get_parts("B X"))))

	print(get_combo(*get_parts("B X")))

	print(
		sum([get_score(*get_combo(*get_parts(r))) for r in test])
	)
	"""

	## part 2
	print("pt 2", sum([get_score(*get_combo(*get_parts(r))) for r in data]))


# a2()

### DAY 1

def a1():
	raw_data = getInput("input1.txt")
	data = [k for k in raw_data.split("\n")]
	print(data[0:15])
	def part1():
		maxm = 0
		summ = 0
		for dp in data:
				if (dp == ""):
					maxm = max(summ, maxm)
					summ = 0
				else:
					summ += int(dp)
		print("max:", maxm)
	def part2():
		maxm = []
		summ = 0
		for dp in data:
				if (dp == ""):
					maxm.append(summ)
					summ = 0
				else:
					summ += int(dp)
		maxm.sort()
		print("max:", maxm[-3:])
		print("sum top 3:", sum(maxm[-3:]))
	part2()

# done
# a1() 