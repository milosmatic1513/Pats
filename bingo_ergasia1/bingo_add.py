import random
def rand_table(final,people):
	
	for i in range(people):
		final.append([])
		for j in range(5):
			final[i].append(random.randint(1,81))
def player_wins(wins,people):
	for i in range(people):
		wins.append(0)


def bingo(people):
	board=range(1,81)
	random.shuffle(board)
	
	final=[]
	wins=[]
	
	rand_table(final,people)
	player_wins(wins,people)

	num_tries=0
	flag=False
	while True:
		number=board.pop(0)
		num_tries+=1
		for i in range(100):
			if(number in final[i]):
				wins[i]+=1
			if (wins[i]==5):
				flag=True
				break
		if (flag==True):
			break
	return num_tries

