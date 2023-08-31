import random

import math

def bitLen(int_type):
	length = 0
	while (int_type):
	    int_type >>= 1
	    length += 1
	return(length)


def BaseRan(b1,b2):
	#while bitLen(total) != 256 :
	s = []
	b = []
	t = []
	aux = 0 
	total = 0
	flag = True 
	while aux < 100:
		if aux == 0 :
			b.append(random.randrange(50,170))
			t.append(random.randrange(50,170))
			s.append(1)
		else :
			minb = b[aux-1]-2
			mint = t[aux-1]-2
			if minb < 0:
				minb = 0
			if mint < 0:
				mint = 0
			if minb != 0 and b[aux-1] != 0:
				b.append(random.randrange(minb,b[aux-1]))
			else :
				b.append(0)
			if mint != 0 and t[aux-1] != 0:
				t.append(random.randrange(mint,t[aux-1]))
			else :
				t.append(0)
			if bitLen(total) > 256 :
				s.append(-1)
			else :
				s.append(1)

		total =  total+s[aux]*(pow(b1,b[aux])*pow(b2,t[aux]))
		aux = aux + 1
		print aux,"----",s[aux-1],b[aux-1],t[aux-1],"----",total,"----",bitLen(total)

	return total

print BaseRan(2,7)


