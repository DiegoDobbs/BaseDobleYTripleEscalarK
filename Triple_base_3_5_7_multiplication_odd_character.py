#Triple-Base Scalar Multiplication in Odd Characteristic > 3

from callcryptolib import *

def ScalarMultiplicationInOdd357(vect,coor,p):

	s = vect['s']
	b = vect['b']
	t = vect['t']
	d = vect['d']
	if s[0] == 1: 
		Z = coor 
	else :
		Z = {'x':coor['x'],'y':(-coor['y'])%p,'z':coor['z']}
	m=len(s)
	z=0
	for i  in range (0,m-1):
		u = b[i]-b[i+1]
		v = t[i]-t[i+1]
		w = d[i]-d[i+1]
		#Z = 7^w Z
		Z = septuplingpow(w,Z,p)
		#Z = 5^t Z
		Z = quintuplingpow(v,Z,p)
		#Z = 3^u Z
		Z = triplingpow(u,Z,p)
		#Z := Z + s[i+1]*P;	
		if s[i+1] == 1: 
			Z = AdditionJacobian(Z,coor,p)
		else :
			Z = AdditionJacobian(Z,{'x':coor['x'],'y':(-coor['y'])%p,'z':coor['z']},p)
	#Z = 7^d[i+1] Z
	Z = septuplingpow(d[i+1],Z,p)
	#Z = 5^t[i+1] Z
	Z = quintuplingpow(t[i+1],Z,p)
	#Z = 3^b[i+1] Z
	Z = triplingpow(b[i+1],Z,p)
	return Z



#def main ():
#	p  = 6277101735386680763835789423207666416083908700390324961279 #numero primo para 192-bits de nivel de seguridad NIST
#	X1 = 3055563715971644849423804859220265481316585815874058627244 #Coordenadas de un punto P en la curva EC.
#	Y1 = 5301271154980119921208363180474818072856515133833450622956
#	Z1 = 1
#	coor = {'x':X1,'y':Y1,'z':Z1}
#
#	s = [1, -1, 1, -1, 1, 1] 
#	b = [1, 1, 1, 0, 0, 0] 
#	t = [0, 0, 0, 0, 0, 0] 
#	d = [6, 4, 3, 3, 0, 0] 
#
#	vect = {'s':s,'b':b,'t':t,'d':d}
#	t0=time.time()
#	Z=ScalarMultiplicationInOdd357(vect,coor,p)
#	t1=time.time()
#	print "time:",(t1-t0),"sec."
#	print affine(Z,p)

#main()

#prime:=6277101735386680763835789423207666416083908700390324961279;
#// prime es un primo de 512 bits de nivel de seguridad NIST.
#print "prime = ", prime;
#F := FiniteField(prime) ; //Definiendo un cuerpo finito |p|_2=192
#a:=F!(-3);
#b:=F!(0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1); 
#E:=EllipticCurve([a,b]);
#print E;
#//P:=Random(E);
#P:=E![3055563715971644849423804859220265481316585815874058627244, 5301271154980119921208363180474818072856515133833450622956];
#print "El punto P= ", P;
#// 895712 = 2^5 3^2 5^5 - 2^2 3^2 5^3 - 2^2 3^2 5^3 +2^0 3^2 5^2 - 2^0 3^1 5^1 + 2^0 3^1 5^0 - 2^0 3^0 5^0 
#s := [1, -1, 1, -1, 1, 1] ;
#b := [1, 1, 1, 0, 0, 0] ;
#t := [0, 0, 0, 0, 0, 0] ;
#d := [6, 4, 3, 3, 0, 0] ;
#a := 3 ^ 1 * 5 ^ 0 * 7 ^ 6 - 3 ^ 1 * 5 ^ 0 * 7 ^ 4 + 3 ^ 1 * 5 ^ 0 * 7 ^ 3 - 3 ^ 0 * 5 ^ 0 * 7 ^ 3 + 3 ^ 0 * 5 ^ 0 * 7 ^ 0 + 3 ^ 0 * 5 ^ 0 * 7 ^ 0 ;
#Z := s[1]*P;
#aux:=0;
#for x in s do 
#    aux:=aux + 1;
#end for;
#for i in [1 .. aux-1] do
#	u := b[i]-b[i+1];
#	v := t[i]-t[i+1];
#	w := d[i]-d[i+1];
#
#	Z := 7^w*Z;
#   Z := 5^v*Z;
#	Z := 3^u*Z;
#	Z := Z + s[i+1]*P;	
#end for;
#Z := 7^d[aux]*Z;
#Z := 5^t[aux]*Z;
#Z := 3^b[aux]*Z;
#print " ";
#print "x =",Z[1];
#print "y =",Z[2];
#print "z =",Z[3];
#print "";
#print a,"P=",a*P;