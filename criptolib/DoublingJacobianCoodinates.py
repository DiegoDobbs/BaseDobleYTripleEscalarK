from ExceptionType import *
from affine import *

def Doubling(coor,p):
  checktype(coor,p)
  #p  = 6277101735386680763835789423207666416083908700390324961279 #numero primo para 192-bits de nivel de seguridad NIST
  X1 = coor['x'] #3055563715971644849423804859220265481316585815874058627244 #Coordenadas de un punto P en la curva EC.
  Y1 = coor['y'] #5301271154980119921208363180474818072856515133833450622956
  Z1 = coor['z'] #1
  #CALCULOS DE LAS FORMULAS EXPLICITAS
  #Calculo de alpha:= 3*(X1+Z1^2)*(X1-Z1^2)*/
  alpha= (3*(X1+pow(Z1,2))*(X1-pow(Z1,2)))%p
  # Fin calculo alpha:= 3*(X1+Z1^2)*(X1-Z1^2) */
  # Calculo de beta:=4*X1*Y1^2 */
  beta = (4*X1*pow(Y1,2))%p
  #FIN Calculo beta:=4*X1*Y1^2*/
  #Calculo X3:=alpha^2-2beta;*/
  X3=(pow(alpha,2)-2*beta)%p
  #FIN Calculo X3:=alpha^2-2beta*/ 
  #Calculo de Y3:=alpha*(beta-X3)-8Y1^4;*/
  Y3 =(alpha*(beta-X3)-8*pow(Y1,4))%p
  #FIN Caclulo Y3:=alpha*(beta-X3)-8*Y1^4*/
  #Calculo de Z3:=2*Y1*Z1*/
  Z3 = (2*Y1*Z1)%p
  return {'x':X3,'y':Y3,'z':Z3}



def Doubling_affine(coor,p):
  return affine(Doubling(coor,p),p)

def Doubling_affiner(coor,p):
  return affiner(Doubling(coor,p),p)


#P  = 115792089210356248762697446949407573530086143415290314195533631308867097853951s
#X1 = 23214596693397255141218547920536253619759004226613097475106265799817441198512s#coor['x']#
#Y1 = 17582485955261531990393572759413304059678227040548071610378634720965647717813s#coor['y']#
#Z1 = 1#coor['z']#
#print " 2P", Doubling_affine({'x':X1,'y':Y1,'z':Z1},P)
#print " 4P", affine(Doubling(Doubling({'x':X1,'y':Y1,'z':Z1},P),P),P)
#print " 8P", affine(Doubling(Doubling(Doubling({'x':X1,'y':Y1,'z':Z1},P),P),P),P)
#print " 16P",affine(Doubling(Doubling(Doubling(Doubling({'x':X1,'y':Y1,'z':Z1},P),P),P),P),P)