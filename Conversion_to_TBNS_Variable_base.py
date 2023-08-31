from callcryptolib import *
from asd import totaal3

b1 = 0
b2 = 0
b3 = 0

def define (k):
	best = pow(k,2)
	for b in range(0, int(ceil(log(k,b1)))+5):
		for t in range(0, int(ceil(log(k,b2)))+5):
			for d in range(0, int(ceil(log(k,b3)))+5):
				z = pow(b1,b)*pow(b2,t)*pow(b3,d)
				if  abs(k-z) <= best:
					best = abs(k-z)
					bt=[b,t,d,z]
	return bt

def definemax (k,tmax,bmax,dmax):
	best = pow(k,2)
	for b in range(0, bmax+1):
		for t in range(0, tmax+1):
			for d in range(0, dmax+1):
				z = pow(b1,b)*pow(b2,t)*pow(b3,d)
				if  abs(k-z) < best:
					best = abs(k-z)
					bt=[b,t,d,z]
	#print "-k-----",k,"z",bt[2],"//b",bt[0],"//t",bt[1],"//best",best
	return bt

def totaal(vectS,vectB,vectT,vectD):
	total = 0
	for i in range (0, len(vectS)):
		total = total + vectS[i]*(pow(b1,vectB[i])*pow(b2,vectT[i])*pow(b3,vectD[i]))
	return int(total)

def resulado (k,vectS,vectB,vectT,vectD):
	print "total:",totaal3(b1,b2,b3,vectS,vectB,vectT,vectD),"///original",k,"///dekta",k-totaal3(b1,b2,b3,vectS,vectB,vectT,vectD)

def dif(k,vectS,vectB,vectT,vectD):
	total = totaal3(b1,b2,b3,vectS,vectB,vectT,vectD)
	if k < total :
		return -1
	else :
		return 1 
def printmagma (vectS,vectB,vectT,vectD):
	for i in range (0,len(vectS)):
		if i == 0 :
			if vectS[i] == 1:
				val = ("a := %d^%d * %d^%d * %d^%d" % (b1, vectB[i], b2, vectT[i], b3, vectD[i]))
			else :
				val = ("a := - %d^%d * %d^%d * %d^%d" % (b1, vectB[i], b2, vectT[i], b3, vectD[i]))
		else :
			if vectS[i] == 1:
				val = val+(" + %d^%d * %d^%d * %d^%d" % (b1, vectB[i], b2, vectT[i], b3, vectD[i]))
			else :
				val = val+(" - %d^%d * %d^%d * %d^%d" % (b1, vectB[i], b2, vectT[i], b3, vectD[i]))
	val = val + (";")
	#print str(val)
	return str(val)

def ConversionToTBNS (k,prin):
	K = k
	vectB = []
	vectT = []
	vectD = []
	vectS = []
	#proxS = 1
	flag = True
	while k > 0:
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
		k = abs(K-totaal3(b1,b2,b3,vectS,vectB,vectT,vectD))
		#resulado(K,vectS,vectB,vectT,vectD)	
	if prin == True :	
		print "s :=",vectS,";"
		print "b :=",vectB,";"
		print "t :=",vectT,";"
		print "d :=",vectD,";"
		print printmagma (vectS,vectB,vectT,vectD)
		resulado(K,vectS,vectB,vectT,vectD)
	else :
		return vectS, vectB, vectT, vectD

# 314159 64564654 437 Conversion to DBNS with restricted exponents

def calltiple (base1,base2,base3,number,pri=False):
	global b1 
	global b2 
	global b3 
	b1 = base1
	b2 = base2
	b3 = base3
	if b1 < b2 and b2 < b3 :
		#print "bases",b1,b2,b3,"//numero ",num
		return ConversionToTBNS(number,pri)
#calltiple (2,3,7,895710,True)
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