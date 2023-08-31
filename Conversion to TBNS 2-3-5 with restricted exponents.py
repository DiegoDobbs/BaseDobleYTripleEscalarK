from callcryptolib import *
from math import *

def define (k):
	best = pow(k,2)
	for b in range(0, int(ceil(log(k,2)))+5):
		for t in range(0, int(ceil(log(k,3)))+5):
			for d in range(0, int(ceil(log(k,5)))+5):
				z = pow(2,b)*pow(3,t)*pow(5,d)
				if  abs(k-z) <= best:
					best = abs(k-z)
					bt=[b,t,d,z]
	return bt

def definemax (k,tmax,bmax,dmax):
	best = pow(k,2)
	for b in range(0, bmax+1):
		for t in range(0, tmax+1):
			for d in range(0, dmax+1):
				z = pow(2,b)*pow(3,t)*pow(5,d)
				if  abs(k-z) < best:
					best = abs(k-z)
					bt=[b,t,d,z]
	#print "-k-----",k,"z",bt[2],"//b",bt[0],"//t",bt[1],"//best",best
	return bt

def totaal (vectS,vectB,vectT,vectD):
	total = 0
	for i in range (0, len(vectS)):
		total = total + vectS[i]*(pow(2,vectB[i])*pow(3,vectT[i])*pow(5,vectD[i]))
	return long(total)

def resulado (k,vectS,vectB,vectT,vectD):
	print "total:",totaal(vectS,vectB,vectT,vectD),"///original",k,"///dekta",k-totaal(vectS,vectB,vectT,vectD)

def dif(k,vectS,vectB,vectT,vectD):
	total = totaal (vectS,vectB,vectT,vectD)
	if k < total :
		return -1
	else :
		return 1 

def ConversionToDBNS (k):
	K = k
	vectB = []
	vectT = []
	vectD = []
	vectS = []
	#proxS = 1
	flag = True
	while abs(K-totaal(vectS,vectB,vectT,vectD)) != 0:
		#define z = 2b 3t , the best approximation of k with 0 <= b <= bmax and 0 <= t <= tmax
		if flag == True:
			flag = False
			bt = define(k)
		else :
			bt = definemax(k,tmax,bmax,dmax)
		z = bt[3]
		bmax = bt[0]
		tmax = bt[1]
		dmax = bt[2]
		vectB.append(bmax)
		vectT.append(tmax)
		vectD.append(dmax)
		vectS.append(dif(K,vectS,vectB,vectT,vectD))
		print (vectS[len(vectS)-1], bt[0], bt[1]),"///", k,"-",z,"=",k-z,"adasdaa",abs(K-totaal(vectS,vectB,vectT,vectD))
		k = abs(K-totaal(vectS,vectB,vectT,vectD))
		resulado(K,vectS,vectB,vectT,vectD)	
			
#	vectS.pop(len(vectS)-1)
	print "s",vectS
	print "b",vectB
	print "t",vectT
	print "d",vectD
	resulado(K,vectS,vectB,vectT,vectD)
# 314159 64564654 437 Conversion to DBNS with restricted exponents
#ConversionToDBNS(9999999999999999)

#	magma
#	s := ;
#	b := ;
#	t := ;
#	d := ;
#	aux := 0;
#	for x in s do 
#	    aux:= aux + 1;
#	end for;
#	k := 0;
#	for i in [1 .. aux] do
#	    k := k+s[i]*(2^b[i]*3^t[i]*5^d[i]);
#	end for;
#	print "real",895712;
#	print k;
#	