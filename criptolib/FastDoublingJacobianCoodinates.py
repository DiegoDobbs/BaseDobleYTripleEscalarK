from ExceptionType import *
from affine import *

def Doubling(coor,p):
	checktype(coor,p)
	#p  = 6277101735386680763835789423207666416083908700390324961279 #numero primo para 192-bits de nivel de seguridad NIST
	X1 = coor['x'] #3055563715971644849423804859220265481316585815874058627244 #Coordenadas de un punto P en la curva EC.
  	Y1 = coor['y'] #5301271154980119921208363180474818072856515133833450622956
  	Z1 = coor['z'] #1

  	alpha = (3*(X1+pow(Z1,2))*(X1-pow(Z1,2)))%p
  	beta = (4*X1*pow(Y1,2))%p

	X3 = (pow(alpha,2)-2*beta)%p
	Y3 = (alpha*(beta-X3)-(8*pow(Y1,4)))%p
	Z3 = (pow((Y1+Z1),2)-pow(Y1,2)-pow(Z1,2))%p

	return {'x':X3,'y':Y3,'z':Z3}
	 
def Doubling_affine(coor,p):
	return affine(Doubling(coor,p),p)

def Doubling_affiner(coor,p):
	return affiner(Doubling(coor,p),p)

#
#P  = 6277101735386680763835789423207666416083908700390324961279
#X1 = 3055563715971644849423804859220265481316585815874058627244#coor['x']#
#Y1 = 5301271154980119921208363180474818072856515133833450622956#coor['y']#
#Z1 = 1#coor['z']#
#
#print Doubling({'x':X1,'y':Y1,'z':Z1},P)
#print Doubling_affine({'x':X1,'y':Y1,'z':Z1},P)