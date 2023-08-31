from ExceptionType import *
from affine import *
from FastDoublingJacobianCoodinates import *
from ThreePJacobianCoordinates import *
from QuintuplingPCoordinates import *
from SeptuplingJ import *

def Print (coor, p, base, exp, aff):
	if  aff == False:
		print base,"pow",exp,"*P =",coor
	elif aff == True:
		print base,"pow",exp,"*P =",affine(coor,p)

def doublingpow(exp,coor,p,imp=False,aff=False):
  	checktype(coor,p)	
	for j in range (0,exp):
		coor = Doubling(coor,p)
		if imp == True:
			Print (coor,p,2,j+1,aff)
	return {'x':coor['x'],'y':coor['y'],'z':coor['z']}

def triplingpow(exp,coor,p,imp=False,aff=False):
  	checktype(coor,p)
	for j in range (0,exp):
		coor = ThreeJacobian(coor,p)
		if imp == True:
			Print (coor,p,3,j+1,aff)
	return {'x':coor['x'],'y':coor['y'],'z':coor['z']}

def quintuplingpow(exp,coor,p,imp=False,aff=False):
  	checktype(coor,p)
	for j in range (0,exp):
		coor = Quintupling(coor,p)
		if imp == True:
			Print (coor,p,5,j+1,aff)
	return {'x':coor['x'],'y':coor['y'],'z':coor['z']}

def septuplingpow(exp,coor,p,imp=False,aff=False):
  	checktype(coor,p)
	for j in range (0,exp):
		coor = Septupling(coor,p)
		if imp == True:
			Print (coor,p,7,j+1,aff)
	return {'x':coor['x'],'y':coor['y'],'z':coor['z']}



#P  = 6277101735386680763835789423207666416083908700390324961279
#X1 = 3055563715971644849423804859220265481316585815874058627244
#Y1 = 5301271154980119921208363180474818072856515133833450622956
#Z1 = 1
#
#print affine(doublingpow(5,{'x':X1,'y':Y1,'z':Z1},P),P)
#print triplingpow(5,{'x':X1,'y':Y1,'z':Z1},P)
#print quintuplingpow(5,{'x':X1,'y':Y1,'z':Z1},P)
#print "qweqwe",affine(septuplingpow(5,{'x':X1,'y':Y1,'z':Z1},P),P)