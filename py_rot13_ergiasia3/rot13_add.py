alph_low=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encode_rot13(x):
	new="";
	length= len(x);
	for i in range(length):
		if (x[i].isalpha()):
			if(x[i].isupper()):
				cap=x[i].lower()
				ind=alph_low.index(cap);
				ind+=13;
				if (ind>25):
					ind-=26;
				new+=alph_low[ind].upper();
			else:
				ind=alph_low.index(x[i]);
				ind+=13;
				if (ind>25):
					ind-=26;
				new+=alph_low[ind];
		else:
			new+=x[i]
	return new;

def decode_rot13(x):
	new="";
	length= len(x);
	for i in range(length):
		if (x[i].isalpha()):
			if(x[i].isupper()):
				cap=x[i].lower()
				ind=alph_low.index(cap);
				ind-=13;
				if (ind>25):
					ind+=26;
				new+=alph_low[ind].upper();
			else:
				ind=alph_low.index(x[i]);
				ind-=13;
				if (ind>25):
					ind+=26;
				new+=alph_low[ind];
		else:
			new+=x[i]
	return new;