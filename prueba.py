from callcryptolib import *

p  = 6277101735386680763835789423207666416083908700390324961279 #numero primo para 192-bits de nivel de seguridad NIST
X1 = 3055563715971644849423804859220265481316585815874058627244 #Coordenadas de un punto P en la curva EC.
Y1 = 5301271154980119921208363180474818072856515133833450622956
Z1 = 1
coor = {'x':X1,'y':Y1,'z':Z1}

triplingpow(6,coor,p,True)


#print "doubling",DoublingJ(coor,p)
#
#print "Fastdoubling",FastDoubling(coor,p)
#
#print "doublingaffine",DoublingJ_affine(coor,p)
#
#print "doublingaffiner",DoublingJ_affiner(coor,p)
#
#print "3j",TreeJacobian(coor,p)
#
#print "3jaffine",TreeJacobian_affine(coor,p)
#
#print "3jaffiner",TreeJacobian_affiner(coor,p)
#
#print "5j",fiveJcobian(coor,p)
#
#print "5jaffine",fiveJcobian_affine(coor,p)
#
#print "5jaffiner",fiveJcobian_affiner(coor,p)	#[1,2,"f"],p)
#
#print RtoL(111,11)
