from ExceptionType import *
from affine import * 

#fast addition
def AdditionJacobian(coor1,coor2,P):
	checktype(coor1,P)
	checktype(coor2,P)
	X1 = coor1['x']
	Y1 = coor1['y']
	Z1 = coor1['z']
	X2 = coor2['x']
	Y2 = coor2['y']
	Z2 = coor2['z']
	
	if X1 == 0 and Y1 == 0 and Z1 == 0 : 
		return {'x':X2,'y':Y2,'z':Z2}
	elif X2 == 0 and Y2 == 0 and Z2 == 0 : 
		return {'x':X1,'y':Y1,'z':Z1}
	else :
		#alpha = (2*(pow(Z1,3)*Y2-pow(Z2,3)*Y1))%P
		#beta  = (pow(Z1,2)*X2-pow(Z2,2)*X1)%P
		#theta = (pow((Z1+Z2),2)-pow(Z1,2)-pow(Z2,2))%P

		#X3    = (pow(alpha,2)-4*pow(beta,3)-8*pow(Z2,2)*X1*pow(beta,2))%P
		#Y3    = (alpha*(pow(Z2,2)*X1*pow(beta,2)-X3)-pow(Z2,3)*Y1*pow(beta,3))%P
		#Z3    = (theta*beta)%P

		alpha = (2*(pow(Z1,3)*Y2-Y1) )%P
		beta  = (pow(Z1,2)*X2-X1)%P
				
		X3    = (pow(alpha,2)-4*pow(beta,3)-8*X1*pow(beta,2))%P
		Y3    = (alpha*(4*X1*pow(beta,2)-X3)-8*Y1*pow(beta,3))%P
		Z3    = (pow((Z1+beta),2)-pow(Z1,2)-pow(beta,2))%P
		#alpha =	(2*(pow(Z1,3)*Y2-pow(Z2,3)*Y1))%P
		#beta  =	(pow(Z1,2)*X2-pow(Z2,2)*X1)%P
		#		 
		#X3    =	(pow(alpha,2)-4*pow(beta,3)-8*pow(Z2,2)*X1*pow(beta,2))%P
		#Y3    =	(alpha*(4*pow(Z2,2)*X1*pow(beta,2)-X3)-8*pow(Z2,3)*Y1*pow(beta,3))%P
		#Z3    =	(2*Z1*Z2*beta)%P


		return {'x':X3,'y':Y3,'z':Z3}
#Normal Function addition
def NormalAdditionJacobian(coor1,coor2,p):
	checktype(coor1,p)
	checktype(coor2,p)
	X1 = coor1['x']
	Y1 = coor1['y']
	Z1 = coor1['z']
	X2 = coor2['x']
	Y2 = coor2['y']
	Z2 = coor2['z']
	
	if X1 == 0 and Y1 == 0 and Z1 == 0 : 
		return {'x':X2,'y':Y2,'z':Z2}
	elif X2 == 0 and Y2 == 0 and Z2 == 0 : 
		return {'x':X1,'y':Y1,'z':Z1}
	else :

		alpha = (pow(Z1,3)*Y2-pow(Z2,3)*Y1)%p
		beta  = (pow(Z1,2)*X2 - pow(Z2,2)*X1)%p
	
		X3    = (pow(alpha,2) - pow(beta,3) - 2*pow(Z2,2)*X1*pow(beta,2))%p
		Y3    = (alpha*(pow(Z2,2)*X1*pow(beta,2) - X3) - pow(Z2,3)*Y1*pow(beta,3))%p
		Z3    = (Z1*beta)%p
	
		return {'x':X3,'y':Y3,'z':Z3}



def AdditionJ_affine(coor,coor2,p):
  return affine(AdditionJacobian(coor,coor2,p),p)

def AdditionJ_affiner(coor,coor2,p):
  return affiner(AdditionJacobian(coor,coor2,p),p)


#def main ():
#	p  = 6277101735386680763835789423207666416083908700390324961279 #numero primo para 192-bits de nivel de seguridad NIST
#	
#	X1 = 1481122789427818349964142174764914763281947104781608149746 #Coordenadas de un punto P en la curva EC.
#	Y1 = 5573819751496129606469472215739749233798682610497754905023
#	Z1 = 1
#	coor2 = {'x':X1,'y':Y1,'z':Z1}
#	X2 = 1481122789427818349964142174764914763281947104781608149746 #Coordenadas de un punto P en la curva EC.
#	Y2 = 5573819751496129606469472215739749233798682610497754905023
#	Z2 = 1
#	coor = {'x':X2,'y':Y2,'z':Z2}
#	print "normal \n",AdditionJacobian(coor,coor2,p)
#	print "fast \n",FastAdditionJacobian(coor,coor2,p)
#main ()
