from Conversion_to_DBNS_Variable_with_restricted_exponents import *
import random 
import numpy
import time 

def mian ():
	tiempo128 = [] 
	tiempo256 = [] 
	tiempo512 = [] 
	scalar = []
	asd = 1 
	max = 1500
	for i in range(0,max):
		print i,"/",max
		ran = True 
		while ran == True :
			if i < 499 :
				aux  = int(random.uniform(170141183460469231731687303715884105728,340282366920938463463374607431768211455))	
			elif i < 999  :
				aux  = int(random.uniform(57896044618658097711785492504343953926634992332820282019728792003956564819968, 115792089237316195423570985008687907853269984665640564039457584007913129639935))
			else :
				aux  = int(random.uniform(6703903964971298549787012499102923063739682910296196688861780721860882015036773488400937149083451713845015929093243025426876941405973284973216824503042048, 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084095))
			if aux not in scalar:
				scalar.append(aux)
				ran = False
		t0=time.time()
		s2, b2, t2 = callDoble (2,3,scalar[i])
		t1=time.time()
		if i < 499 :
			tiempo128.append((t1-t0))
		elif i < 999  :
			tiempo256.append((t1-t0))
		else :
			tiempo512.append((t1-t0))

	print "128 bits promedio :",numpy.mean(tiempo128)," desviacion estandar :",numpy.std(tiempo128)
	print "256 bits promedio :",numpy.mean(tiempo256)," desviacion estandar :",numpy.std(tiempo256)
	print "512 bits promedio :",numpy.mean(tiempo512)," desviacion estandar :",numpy.std(tiempo512)

mian ()

#500 experimentos cada una	
#128 bits promedio : 0.0222332348566  desviacion estandar : 0.00580247570159
#256 bits promedio : 0.105503564835  desviacion estandar : 0.0448045645416
#512 bits promedio : 0.762397289276  desviacion estandar : 0.410341390412
