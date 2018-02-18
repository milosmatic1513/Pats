
import twitter_add

while True:
	
	while True:
		try:
			user=raw_input("Please enter user (type 'exit' to exit): ")
			timeline = twitter_add.get_timeline(user)
			if( user=="exit"):
				break
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
			while True:
				ans=raw_input("would you like to see the tweets?(y/n):")
				if (ans=="y"):
					for i in range(10):
						temp=table[i].split(" ")
						print i+1,")",;
						for word in temp:
							try:
								print word ,
							except UnicodeError:
								pass
						print "\n"
					break
				elif (ans=="n"):
					break
			break
		except:
			if (user=="exit"):
				break
			else:
				print "user not found"
	break
