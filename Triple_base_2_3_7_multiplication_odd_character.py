#Triple-Base Scalar Multiplication in Odd Characteristic > 3

from callcryptolib import *
#from Conversion_to_TBNS_Variable_base import *

def ScalarMultiplicationInOdd237(vect,coor,p):

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
		#Z = 3^v Z
		Z = triplingpow(v,Z,p)
		#Z = 2^u Z
		Z = doublingpow(u,Z,p)
		#Z := Z + s[i+1]*P;	
		if s[i+1] == 1: 
			Z = AdditionJacobian(Z,coor,p)
		else :
			Z = AdditionJacobian(Z,{'x':coor['x'],'y':(-coor['y'])%p,'z':coor['z']},p)
	#Z = 7^d[i+1] Z
	Z = septuplingpow(d[i+1],Z,p)
	#Z = 3^t[i+1] Z
	Z = triplingpow(t[i+1],Z,p)
	#Z = 2^b[i+1] Z
	Z = doublingpow(b[i+1],Z,p)
	return Z



#def main ():
#	s  = 68759779829300857076289944435166577427782710722564810660205763491176130805760
#	p  = 115792089210356248762697446949407573530086143415290314195533631308867097853951#numero primo para 192-bits de nivel de seguridad NIST
#	X1 = 23214596693397255141218547920536253619759004226613097475106265799817441198512 #Coordenadas de un punto P en la curva EC.
#	Y1 = 17582485955261531990393572759413304059678227040548071610378634720965647717813
#	Z1 = 1
#	coor = {'x':X1,'y':Y1,'z':Z1}
#	s3, b3, t3, d3 =  calltiple (2,3,7,s)
#	v237 = {'s':s3,'b':b3,'t':t3,'d':d3}
#	t0=time.time()
#	Z=ScalarMultiplicationInOdd237(v237,coor,p)
#	t1=time.time()
#	print "time:",(t1-t0),"sec."
#	print affine(Z,p)
#
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
#s:=[1,-1,-1,1,-1,1,-1];
#b:=[5,2,2,0,0,0,0];
#c:=[2,2,2,2,1,1,0];
#d:=[5,3,3,2,1,0,0];
#a := 2^5*3^2*7^5 - 2^2*3^2*7^3 - 2^2*3^2*7^3 +2^0*3^2*7^2 - 2^0*3^1*7^1 + 2^0*3^1*7^0 - 2^0*3^0*7^0;
#
#Z := s[1]*P;
#aux:=0;
#for x in s do
#    aux:=aux + 1;
#end for;
#for i in [1 .. aux-1] do
#    u := b[i]-b[i+1];
#    v := c[i]-c[i+1];
#    w := d[i]-d[i+1];
#
#    Z := 7^w*Z;
#    Z := 3^v*Z;
#    Z := 2^u*Z;
#    Z := Z + s[i+1]*P;   
#end for;
#Z := 7^d[aux]*Z;
#Z := 3^c[aux]*Z;
#Z := 2^b[aux]*Z;
#print " ";
#print "x =",Z[1];
#print "y =",Z[2];
#print "z =",Z[3];
#print "";
#print a,"P=",a*P;