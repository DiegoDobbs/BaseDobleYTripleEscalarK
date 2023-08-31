from callcryptolib import *
from asd import totaal2

b1 = 0
b2 = 0
def define (k):
	best = pow(k,2)
	for b in range(0, int(ceil(log(k,b1)))+5):
		for t in range(0, int(ceil(log(k,b2)))+5):
			z = pow(b1,b)*pow(b2,t)
			if  abs(k-z) <= best:
				best = abs(k-z)
				bt=[b,t,z]
	return bt

def definemax (k,tmax,bmax):
	best = pow(k,2)
	for b in range(0, bmax+1):
		for t in range(0, tmax+1):
			z = pow(b1,b)*pow(b2,t)
			if  abs(k-z) < best:
				best = abs(k-z)
				bt=[b,t,z]
	return bt

def totaal (vectS,vectB,vectT):
	total = 0
	for i in range (0, len(vectS)):
		total = total + vectS[i]*(pow(b1,vectB[i])*pow(b2,vectT[i]))
	return int(total)

def resulado (k,vectS,vectB,vectT):
	print "total:",totaal2(b1,b2,vectS,vectB,vectT),"///original",k,"///dekta",k-totaal2 (b1,b2,vectS,vectB,vectT)

def dif(k,vectS,vectB,vectT):
	total = totaal2 (b1,b2,vectS,vectB,vectT)
	if k < total :
		return -1
	else :
		return 1 

def printmagma (vectS,vectB,vectT):
	for i in range (0,len(vectS)):
		if i == 0 :
			if vectS[i] == 1:
				print "a :=",b1,"^",vectB[i],"*",b2,"^",vectT[i],
			else :
				print "a := -",b1,"^",vectB[i],"*",b2,"^",vectT[i],
		else :
			if vectS[i] == 1:
				print "+",b1,"^",vectB[i],"*",b2,"^",vectT[i],
			else :
				print "-",b1,"^",vectB[i],"*",b2,"^",vectT[i],
	print ";\n"


def ConversionToDBNS (k,pri):
	K = k
	vectB = []
	vectT = []
	vectS = []
	#proxS = 1
	flag = True
	while k > 0  :
		#define z = 2b 3t , the best approximation of k with 0 <= b <= bmax and 0 <= t <= tmax
		if flag == True:
			bt = define(k)
		else :
			bt = definemax(k,tmax,bmax)
		z = bt[2]
		bmax = bt[0]
		tmax = bt[1]
		vectB.append(bmax)
		vectT.append(tmax)
		if flag == True:
			flag = False
			vectS.append(1)
		else :
			vectS.append(dif(K,vectS,vectB,vectT))
		k = abs(K-totaal2(b1,b2,vectS,vectB,vectT))
		#resulado(K,vectS,vectB,vectT)	
	
	if pri == True:
		print "s := ",vectS,";"
		print "b := ",vectB,";"
		print "t := ",vectT,";"
		printmagma (vectS,vectB,vectT)
		resulado(K,vectS,vectB,vectT)
	else :
		return vectS, vectB, vectT

def callDoble (base1,base2,number,pri=False):
	global b1 
	global b2 
	b1 = base1
	b2 = base2
	if b1 < b2:
		return	ConversionToDBNS(number,pri)
#callDoble(2,3,895710,True )

#	magma
#	s := [1, -1, -1, -1, -1, -1];
#	b := [4, 0, 0, 0, 0, 0];
#	t := [9, 6, 3, 2, 1, 0];
#	aux := 0;
#	for x in s do 
#	    aux:= aux + 1;
#	end for;
#	k := 0;
#	for i in [1 .. aux] do
#	    k := k+s[i]*(2^b[i]*3^t[i]);
#	end for;
#	print "real",895712;
#	print k;
#	