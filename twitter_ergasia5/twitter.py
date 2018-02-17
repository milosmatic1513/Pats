
import twitter_add

while True:
	
	while True:
		try:
			user=raw_input("Please enter user : ")
			timeline = twitter_add.get_timeline(user)

			table=[]
			for line in timeline:
				table.append(line.text)
			new_table=[]
			temp=[]
			for line in table:
				temp=line.split(" ")
				for word in temp:
					new_table.append(word)

			just_words=[]
			for word in new_table:
				if word not in just_words:
					just_words.append(word)

			word_times=[]
			for word in just_words:
				word_times.append(new_table.count(word))
			max_word=max(word_times)

			print "The most repeated word(s) :"
			for i in range(len(word_times)):
				if(word_times[i]==max_word):
					print "-"+just_words[i]
			break
		except:
			print "user not found"
	break
