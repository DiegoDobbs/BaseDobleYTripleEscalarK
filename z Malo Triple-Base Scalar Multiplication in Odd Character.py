from callcryptolib import *

s=[1,1,1,1,1,1]
b=[4,4,4,1,0,0]
c=[7,5,4,4,2,1]
d=[2,1,0,0,0,0]

def ScalarTripleBaseMultiplicationInOdd(coor,p):
	if s[0] == 1: 
		Z = coor 
	else :
		Z = {'x':coor['x'],'y':(-coor['y'])%p,'z':coor['z']}
	m=len(s)
	for i  in range (0,m-1):
		u = b[i]-b[i+1]
		v = c[i]-c[i+1]
		w = d[i]-d[i+1]
		if u == 0 :
			#Z= 5^w*Z
			for j in range (0,w):
				Z = Quintupling_affine(Z,p)
			if v != 0 :
				#Z= 3(3^(v-1)*Z)+s[i+1]P
				for j in range (0,v-1):
					Z = ThreeJacobian_affine(Z,p)#3^(v-1)*Z
				Z = ThreeJacobian_affine(Z,p)#3(3^(v-1)*Z)
				if s[i+1] == 1: #+s[i+1]P
					Z = affine(AdditionJacobian(Z,coor,p),p)
				else :
					Z = affine(AdditionJacobian(Z,{'x':coor['x'],'y':(-coor['y'])%p,'z':coor['z']},p),p)
			else :
				if s[i+1] == 1: 
					Z = affine(AdditionJacobian(Z,coor,p),p)
				else :
					Z = affine(AdditionJacobian(Z,{'x':coor['x'],'y':(-coor['y'])%p,'z':coor['z']},p),p)
		else :
			#Z= 5^w*Z
			for j in range (0,w):
				Z = Quintupling_affine(Z,p)
			for j in range (0,v):
				Z = ThreeJacobian_affine(Z,p)#3^(v)*Z
			#Z = 2^(u-1)*Z
			for j in range (0,u-1):
				Z = Doubling_affine(Z,p)
		#Z = 2Z + S[i+1]P
		Z = Doubling_affine(Z,p)
		if s[i+1] == 1: 
			Z = affine(AdditionJacobian(Z,coor,p),p)
		else :
			Z = affine(AdditionJacobian(Z,{'x':coor['x'],'y':(-coor['y'])%p,'z':coor['z']},p),p)
	return Z


def main ():
	p  = 6277101735386680763835789423207666416083908700390324961279 #numero primo para 192-bits de nivel de seguridad NIST
	X1 = 3055563715971644849423804859220265481316585815874058627244 #Coordenadas de un punto P en la curva EC.
	Y1 = 5301271154980119921208363180474818072856515133833450622956
	Z1 = 1
	coor = {'x':X1,'y':Y1,'z':Z1}
	t0=time.time()
	Z=ScalarTripleBaseMultiplicationInOdd(coor,p)
	t1=time.time()
	print "time:",(t1-t0),"sec."
	print Z

main()

#
# 895712 = 2^4 3^7 5^2 + 2^4 3^5 5^1 + 2^4 3^4 5^0 + 2^1 3^4 5^0 + 2^0 3^2 5^0 + 2^0 3^1 5^0 probar 
#Fast Scalar Multiplication in ECC Using The Multi base Number System
#G. N. Purohit, Asmita Singh Rawat
# page 9