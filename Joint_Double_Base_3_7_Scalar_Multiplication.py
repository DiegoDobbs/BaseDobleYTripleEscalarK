	#Double-Base Scalar Multiplication in Odd Characteristic > 3
#314159P = 3^15 7^2 P + 3^11 7^2 P + 3^8 7^1 P + 3^4 7^1 P - 3^0 7^0P
from callcryptolib import *

def JointScalarMultiplication37(vect,coor,coor2,p):
	s1 = vect['s1']
	s2 = vect['s2']
	b = vect['b']
	t = vect['t']

	#pre-calculos 
	# p + q (1 1)
	T1 = AdditionJ_affine(coor,coor2,p)
	# p  (1 0)
	# q  (0 1)
	# p - q  (1 -1)
	T2 = AdditionJ_affine(coor,{'x':coor2['x'],'y':(-coor2['y'])%p,'z':coor2['z']},p)
	# - p + q  (-1 1)
	T3 = {'x':T2['x'],'y':(-T2['y'])%p,'z':T2['z']}
	# - p - q  (-1 -1)
	T4 = {'x':T1['x'],'y':(-T1['y'])%p,'z':T1['z']}	
	# p  (-1 0)
	T5 = {'x':coor['x'],'y':(-coor['y'])%p,'z':coor['z']}	
	# q  (0 -1)
	T6 = {'x':coor2['x'],'y':(-coor2['y'])%p,'z':coor2['z']}

	m=len(s1)
	for i  in range (0,m-1):
		u = b[i]-b[i+1]
		v = t[i]-t[i+1]
		if i == 0 :
			if s1[i] == 1 and s2[i] == 1 :
				Z = septuplingpow(v,T1,p)
			elif s1[i] == 1 and s2[i] == 0 :
				Z = septuplingpow(v,coor,p)
			elif s1[i] == 0 and s2[i] == 1 :
				Z = septuplingpow(v,coor2,p)
			elif s1[i] == 1 and s2[i] == -1 :
				Z = septuplingpow(v,T2,p)
			elif s1[i] == -1 and s2[i] == 1 :
				Z = septuplingpow(v,T3,p)
			elif s1[i] == -1 and s2[i] == -1 :
				Z = septuplingpow(v,T4,p)
			elif s1[i] == -1 and s2[i] == 0 :
				Z = septuplingpow(v,T5,p)
			elif s1[i] == 0 and s2[i] == -1 :
				Z = septuplingpow(v,T6,p)
			elif s1[i] == 0 and s2[i] == 0 :
				Z = {'x':long(0),'y':long(0),'z':long(0)}
			Z = triplingpow(u,Z,p)
		else :
			#Z = 7^v Z
			Z = septuplingpow(v,Z,p)
			#Z = 3^u Z
			Z = triplingpow(u,Z,p)
		if   s1[i+1] == 1 and s2[i+1] == 1 :
			if Z['x'] == T1['x'] and abs(Z['y']) == abs(T1['y']) and Z['z'] == T1['z']:
				Z = Doubling(Z,p)
			else :
				Z = AdditionJacobian(Z,T1,p)
		elif s1[i+1] == 1 and s2[i+1] == 0 :
			if Z['x'] == coor['x'] and abs(Z['y']) == abs(coor['y']) and Z['z'] == coor['z']:
				Z = Doubling(Z,p)
			else :
				Z = AdditionJacobian(Z,coor,p)
		elif s1[i+1] == 0 and s2[i+1] == 1 :
			if Z['x'] == coor2['x'] and abs(Z['y']) == abs(coor2['y']) and Z['z'] == coor2['z']:
				Z = Doubling(Z,p)
			else :
				Z = AdditionJacobian(Z,coor2,p)
		elif s1[i+1] == 1 and s2[i+1] == -1 :
			if Z['x'] == T2['x'] and abs(Z['y']) == abs(T2['y']) and Z['z'] == T2['z']:
				Z = Doubling(Z,p)
			else :
				Z = AdditionJacobian(Z,T2,p)
		elif s1[i+1] == -1 and s2[i+1] == 1 :
			if Z['x'] == T3['x'] and abs(Z['y']) == abs(T3['y']) and Z['z'] == T3['z']:
				Z = Doubling(Z,p)
			else :
				Z = AdditionJacobian(Z,T3,p)
		elif s1[i+1] == -1 and s2[i+1] == -1 :
			if Z['x'] == T4['x'] and abs(Z['y']) == abs(T4['y']) and Z['z'] == T4['z']:
				Z = Doubling(Z,p)
			else :
				Z = AdditionJacobian(Z,T4,p)
		elif s1[i+1] == -1 and s2[i+1] == 0 :
			if Z['x'] == T5['x'] and abs(Z['y']) == abs(T5['y']) and Z['z'] == T5['z']:
				Z = Doubling(Z,p)
			else :
				Z = AdditionJacobian(Z,T5,p)
		elif s1[i+1] == 0 and s2[i+1] == -1 :
			if Z['x'] == T6['x'] and abs(Z['y']) == abs(T6['y']) and Z['z'] == T6['z']:
				Z = Doubling(Z,p)
			else :
				Z = AdditionJacobian(Z,T6,p)
			
	#Z = 7^t[i+1] Z
	Z = septuplingpow(t[i+1],Z,p)
	#Z = 3^b[i+1] Z
	Z = triplingpow(b[i+1],Z,p)
	return Z

#def main ():
#	p  = 6277101735386680763835789423207666416083908700390324961279 #numero primo para 192-bits de nivel de seguridad NIST
#	
#	X1 = 3055563715971644849423804859220265481316585815874058627244 #Coordenadas de un punto P en la curva EC.
#	Y1 = 5301271154980119921208363180474818072856515133833450622956
#	Z1 = 1
#	coor = {'x':X1,'y':Y1,'z':Z1}
#	X2 = 3366172135749127752442661849960622274110712161924290025866 #Coordenadas de un punto P en la curva EC.
#	Y2 = 6139723457849173165011744227944843453513622199649544688473
#	Z2 = 1
#	coor2 = {'x':X2,'y':Y2,'z':Z2}
#	JDBC(3,7,a,b,True)
#	sb1, sb2, b2, c2 = JDBC(3,7,a,b)
#	vect = {'s1':s1,'s2':s2,'b':b,'t':t}
#	#print "punto P",coor,"\n"
#	t0=time.time()
#	Z=JointScalarMultiplication37(vect,coor,coor2,p)
#	t1=time.time()
#	print "time:",(t1-t0),"sec."
#	print affine(Z,p)
#main ()
#
#prime:=6277101735386680763835789423207666416083908700390324961279;
#// prime es un primo de 512 bits de nivel de seguridad NIST.
#print "prime = ", prime;
#F := FiniteField(prime) ; //Definiendo un cuerpo finito |p|_2=192
#a:=F!(-3);
#b:=F!(0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1); 
#
#E:=EllipticCurve([a,b]);
#print E;
#
#//P:=Random(E);
#P:=E![3055563715971644849423804859220265481316585815874058627244, 5301271154980119921208363180474818072856515133833450622956];
#Q:=E![3366172135749127752442661849960622274110712161924290025866, 6139723457849173165011744227944843453513622199649544688473];
#print "El punto P= ", P;
#print "El punto Q= ", Q;
#
#s1 := [1, 1, 1, 0, 0];
#s2 := [1, -1, 1, 1, -1];
#b :=  [3, 3, 2, 1, 0];
#t :=  [1, 0, 0, 0, 0];
#a :=  ( 1 ) * ( 3 ^ 3 * 7 ^ 1 )  +  ( 1 ) * ( 3 ^ 3 * 7 ^ 0 )  +  (  1 ) * ( 3 ^ 2 * 7 ^ 0 )  +  ( 0 ) * ( 3 ^ 1 * 7 ^ 0 )  +  ( 0 ) * ( 3 ^ 0 * 7 ^ 0 );
#k :=  ( 1 ) * ( 3 ^ 3 * 7 ^ 1 )  +  ( -1 ) * ( 3 ^ 3 * 7 ^ 0 )  +  ( 1 ) * ( 3 ^ 2 * 7 ^ 0 )  +  ( 1 ) * ( 3 ^ 1 * 7 ^ 0 )  +  ( -1 ) * ( 3 ^ 0 * 7 ^ 0 );
#print " ";
#aux:=0;
#for x in s1 do 
#    aux:=aux + 1;
#end for;
#for i  in [1 .. aux-1] do
#	u := b[i]-b[i+1];
#	v := t[i]-t[i+1];
#	if i eq 1 then 
#        if s1[i] eq 1 and  s2[i] eq 1 then 
#			Z := 7^v*P+Q;
#		end if ;
#		if s1[i] eq 1 and  s2[i] eq 0 then 
#			Z := 7^v*P;
#		end if ;
#		if s1[i] eq 0 and  s2[i] eq 1 then 
#			Z := 7^v*Q;
#		end if ;
#		if s1[i] eq 1 and  s2[i] eq -1 then 
#			Z := 7^v*P-Q;
#		end if ;
#		if s1[i] eq -1 and  s2[i] eq 1 then 
#			Z := 7^v*-P+Q;
#		end if ;
#		if s1[i] eq -1 and  s2[i] eq -1 then 
#			Z := 7^v*-P-Q;
#		end if ;
#		if s1[i] eq -1 and  s2[i] eq 0 then 
#			Z := 7^v*-P;
#		end if ;
#		if s1[i] eq 0 and  s2[i] eq -1 then 
#			Z := 7^v*-Q;
#		end if ;
#        Z := 3^u*Z;
#    else 
#        Z := 7^v*Z;
#        Z := 3^u*Z;
#    end if;
#	if s1[i+1] eq 1 and  s2[i+1] eq 1 then 
#		Z := Z + P+Q;
#	end if ;
#	if s1[i+1] eq 1 and  s2[i+1] eq 0 then 
#		Z := Z + P;
#	end if ;
#	if s1[i+1] eq 0 and  s2[i+1] eq 1 then 
#		Z := Z + Q;
#	end if ;
#	if s1[i+1] eq 1 and  s2[i+1] eq -1 then 
#		Z := Z + P-Q;
#	end if ;
#	if s1[i+1] eq -1 and  s2[i+1] eq 1 then 
#		Z := Z + -P+Q;
#	end if ;
#	if s1[i+1] eq -1 and  s2[i+1] eq -1 then 
#		Z := Z + -P-Q;
#	end if ;
#	if s1[i+1] eq -1 and  s2[i+1] eq 0 then 
#		Z := Z + -P;
#	end if ;
#	if s1[i+1] eq 0 and  s2[i+1] eq -1 then 
#		Z := Z + -Q;
#	end if ;
#
#end for;
#Z := 7^t[aux]*Z;
#Z := 3^b[aux]*Z;
#print " ";
#print "x =",Z[1];
#print "y =",Z[2];
#print "z =",Z[3];
#print a,"*P+",k,"*Q=",a*P+k*Q;