import rot13_add
final="";

while True:
	ans=raw_input("Would you like to read from a file or directly input the text? (file/text)")
	if (ans=="file"):
		while True:
			try:
				input_file=raw_input("Input file to read from")
				inp=open(input_file,"r")
				break
			except:
				print "file not found"
		break
	elif(ans=="text"):
		inp=raw_input("Input text")
		break


while True:
	ans=raw_input("Whould you like to encrypt or decrypt in rot13? (en/de)")
	if(ans=="en"):
		for line in inp:
			final+=rot13_add.encode_rot13(line);
		print final
		break
	elif(ans=="de"):
		for line in inp:
			final+=rot13_add.decode_rot13(line);
		print final
		break

