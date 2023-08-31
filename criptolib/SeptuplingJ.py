from ExceptionType import *
from affine import *

def Septupling(coor,P):
	checktype(coor,P)
	X1 = coor['x']
	Y1 = coor['y']
	Z1 = coor['z']
	a = -3 

	alpha = (3*pow(X1,2)+a*pow(Z1,4))%P
	X11   = (2*(pow((X1+pow(Y1,2)),2)-pow(X1,2)-pow(Y1,4)))%P
	#X11  = (4*X1*pow(Y1,2))%P
	#alpha= (3*(X1+pow(Z1,2)*(X1-pow(Z1,2))%P
	Z2    = (pow((Y1+Z1),2)-pow(Y1,2)-pow(Z1,2))%P
	YY11  = (16*pow(Y1,4))%P
	X2    = (pow(alpha,2)-2*X11)%P
	theta = (X11-X2)%P
	YY2   = (pow((alpha+theta),2)-pow(alpha,2)-pow(theta,2)-YY11)%P
	Y21   = (4*YY2*pow(theta,3))%P
	X21   = (4*X2*pow(theta,2))%P
	omega = (YY11 - YY2)%P
	phi	  = (pow(omega,2)-4*pow(theta,3)-3*X21)%P
	Z22	  = (2*Z2*(pow((theta+phi),2)-pow(theta,2)-pow(phi,2)))%P
	Y22   = (8*Y21*pow(phi,3))%P
	X22	  = (4*X21*pow(phi,2))%P
	gamma = (pow(omega,2)+pow(phi,2)-pow((omega+phi),2)-4*Y21)%P
	sigma = (pow(gamma,2)-4*pow(phi,3)-3*X22)%P
	varphi= (pow(gamma,2)+pow(sigma,2)-pow((gamma+sigma),2)-4*Y22)%P
		
	X7 = (pow(varphi,2)-4*pow(sigma,3)-8*X22*pow(sigma,2))%P
	Y7 = (varphi*(4*X22*pow(sigma,2)-X7)-8*Y22*pow(sigma,3))%P
	Z7 = (2*Z22*sigma)%P

	return {'x':X7,'y':Y7,'z':Z7}


def Septupling_affine(coor,p):
    coor=affine(Septupling(coor,p),p)
    return(coor)

def Septupling_affiner(coor,p):
    coor=affiner(Septupling(coor,p),p)
    return(coor)

#P  = 6277101735386680763835789423207666416083908700390324961279
#X1 = 3055563715971644849423804859220265481316585815874058627244#coor['x']#
#Y1 = 5301271154980119921208363180474818072856515133833450622956#coor['y']#
#Z1 = 1#coor['z']#
#
#print Septupling({'x':X1,'y':Y1,'z':Z1},P)
#print "7P", Septupling_affine({'x':X1,'y':Y1,'z':Z1},P)
#print "49 P", affine(Septupling(Septupling({'x':X1,'y':Y1,'z':Z1},P),P),P)
#print "343 P", affine(Septupling(Septupling(Septupling({'x':X1,'y':Y1,'z':Z1},P),P),P),P)
#print "2401 P", affine(Septupling(Septupling(Septupling(Septupling({'x':X1,'y':Y1,'z':Z1},P),P),P),P),P)
#print "16807 P", affine(Septupling(Septupling(Septupling(Septupling(Septupling({'x':X1,'y':Y1,'z':Z1},P),P),P),P),P),P)
#print "117649 P", affine(Septupling(Septupling(Septupling(Septupling(Septupling(Septupling({'x':X1,'y':Y1,'z':Z1},P),P),P),P),P),P),P)

#
# Fast Multibase Methods and Other Several Optimizations for Elliptic Curve Scalar Multiplication
#Patrick Longa and Catherine Gebotys
# page 18 and 19
#