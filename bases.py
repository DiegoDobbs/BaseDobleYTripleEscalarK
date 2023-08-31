
from Conversion_to_TBNS_Variable_base import *
import random 

def pvect(vect):
	pri =("[")
	for i in range(0,len(vect)):
		pri=pri+("%d"%vect[i])
		if len(vect)-1 != i:
			pri=pri+(",")
	pri=pri+("];")
	return str(pri)

def oli ():
	f = open('basea', 'w')
	scalar = []
	ran = True 
	for i in range(0,100):
		while ran == True :
				aux = int(random.uniform(10000000, 10000000000000))
				if aux not in scalar:
					scalar.append(aux)
					ran = False
		ran = True 
		f.write("------------------%d---------------------------------------------------------------------------------\n"%i)
		f.write(str("valor := %d;" % scalar[i]))
		f.write("\n")
		vectS, vectB, vectT, vectD =  calltiple(2,3,5,scalar[i])	
		f.write(str("s := "+pvect(vectS)))
		f.write("\n")
		f.write(str("b := "+pvect(vectB)))
		f.write("\n")
		f.write(str("c := "+pvect(vectT)))
		f.write("\n")
		f.write(str("d := "+pvect(vectD)))
		f.write("\n")
		k = printmagma(vectS,vectB,vectT,vectD)
		f.write(k)
		f.write("\n")
		

oli()