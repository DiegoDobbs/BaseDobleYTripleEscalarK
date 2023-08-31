
def totaal2 (b1,b2,vectS,vectB,vectT):
	total = 0
	for i in range (0, len(vectS)):
		total = total + vectS[i]*(pow(b1,vectB[i])*pow(b2,vectT[i]))
	return long(total)

def totaal3 (b1,b2,b3,vectS,vectB,vectT,vectD):
	total = 0
	for i in range (0, len(vectS)):
		total = total + vectS[i]*(pow(b1,vectB[i])*pow(b2,vectT[i])*pow(b3,vectD[i]))
	return long(total)

