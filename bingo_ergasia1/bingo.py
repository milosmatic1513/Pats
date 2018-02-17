import bingo_add
people=100
sum=0
for i in range(1000):
	sum+=bingo_add.bingo(people)

string_num=str((sum/1000.0))

print ("Meso oros arithmon mexri to BINGO :")+string_num

