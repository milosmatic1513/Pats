import random
def rand_table(lines,rows):
	table=[]
	alph=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	for i in range (lines):
		table.append([])
		for j in range(rows):
			table[i].append(random.choice(alph))
	return table