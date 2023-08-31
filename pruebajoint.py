from callcryptolib import *
from Join_double_base_number_system_base import *
from Joint_Double_Base_2_3_Scalar_Multiplication import *
from Joint_Double_Base_2_5_Scalar_Multiplication import *
from Joint_Double_Base_2_7_Scalar_Multiplication import *
from Joint_Double_Base_3_5_Scalar_Multiplication import *
from Joint_Double_Base_3_7_Scalar_Multiplication import *
from Joint_Double_Base_5_7_Scalar_Multiplication import *
import random 

import numpy
falsos = 0 
def compJoint(ZJoint23,ZJoint25,ZJoint27,ZJoint35,ZJoint37,ZJoint57,P):
	if affine(ZJoint23,P)!=affine(ZJoint25,P):
		print "25"
	if affine(ZJoint23,P)!=affine(ZJoint27,P):
		print "27"
	if affine(ZJoint23,P)!=affine(ZJoint35,P):
		print "35"
	if affine(ZJoint23,P)!=affine(ZJoint37,P):
		print "37"
	if affine(ZJoint23,P)!=affine(ZJoint57,P):
		print "57"
	if affine(ZJoint23,P)==affine(ZJoint25,P)==affine(ZJoint27,P)==affine(ZJoint35,P)==affine(ZJoint37,P)==affine(ZJoint57,P):
		 print True
	else :
		print  False
		falsos = falsos + 1
def asd():
	scalar = []
	ZJoint23 = []
	ZJoint25 = []
	ZJoint27 = []
	ZJoint35 = []
	ZJoint37 = []
	ZJoint57 = []
	#vectores de joint 
	sb1 = []
	sb2 = []
	b2  = []
	c2  = []
	p  = 115792089210356248762697446949407573530086143415290314195533631308867097853951	 #numero primo para 256-bits de nivel de seguridad NIST
	X1 = 23214596693397255141218547920536253619759004226613097475106265799817441198512 #Coordenadas de un punto P en la curva EC.
	Y1 = 17582485955261531990393572759413304059678227040548071610378634720965647717813
	Z1 = 1
	X2 = 98412530668235200848772828508190622194068156824181695326117330679756264623647
	Y2 = 50852179810991374232999932859585543263140189651850993040851792664262650594978
	Z2 = 1
	max = 10000 #~######################################################
	coor = {'x':X1,'y':Y1,'z':Z1}
	coor2 = {'x':X2,'y':Y2,'z':Z2}
	for i in range(0,max):
		print int(((i+1)*100)/max),"% ",i+1,"/",max
		#define escalar ran es para calcualr cuando saco el escalar
		ran = True 
		while ran == True :
			aux  = int(random.uniform(10   ,100))
			aux2 = int(random.uniform(101,200))
			if aux not in scalar and aux2 not in scalar :
				scalar.append([aux,aux2])
				ran = False
		#calcula los vectores
		#print " 2-3,",
		sb1, sb2, b2, c2 = JDBC(2,3,scalar[i][0],scalar[i][1])
		vD23  = {'s1':sb1,'s2':sb2,'b':b2,'t':c2}
		#calcula el la clave y o
		ZJoint23.append(JointScalarMultiplication23(vD23,coor,coor2,p))
		#----------------------------base 2-5------------------------------------------#
		#calcula los vectores
		#print " 2-5,",
		sb1, sb2, b2, c2 = JDBC(2,5,scalar[i][0],scalar[i][1])
		vD25  = {'s1':sb1,'s2':sb2,'b':b2,'t':c2}
		#calcula el la clave y o
		ZJoint25.append(JointScalarMultiplication25(vD25,coor,coor2,p))
		#----------------------------base 2-7------------------------------------------#
		#calcula los vectores
		#print " 2-7,",
		sb1, sb2, b2, c2 = JDBC(2,7,scalar[i][0],scalar[i][1])
		vD27  = {'s1':sb1,'s2':sb2,'b':b2,'t':c2}
		#calcula el la clave y o
		ZJoint27.append(JointScalarMultiplication27(vD27,coor,coor2,p))
		#----------------------------base 3-5------------------------------------------#
		#calcula los vectores
		#print " 3-5,",
		sb1, sb2, b2, c2 = JDBC(3,5,scalar[i][0],scalar[i][1])
		vD35  = {'s1':sb1,'s2':sb2,'b':b2,'t':c2}
		#calcula el la clave y o
		ZJoint35.append(JointScalarMultiplication35(vD35,coor,coor2,p))
		#----------------------------base 3-7------------------------------------------#
		#calcula los vectores
		#print " 3-7,",
		sb1, sb2, b2, c2 = JDBC(3,7,scalar[i][0],scalar[i][1])
		vD37  = {'s1':sb1,'s2':sb2,'b':b2,'t':c2}
		#calcula el la clave y o
		ZJoint37.append(JointScalarMultiplication37(vD37,coor,coor2,p))
		#----------------------------base 5-7------------------------------------------#
		#calcula los vectores
		#print " 5-7,",
		sb1, sb2, b2, c2 = JDBC(5,7,scalar[i][0],scalar[i][1])
		vD57  = {'s1':sb1,'s2':sb2,'b':b2,'t':c2}
		#calcula el la clave y o
		ZJoint57.append(JointScalarMultiplication57(vD57,coor,coor2,p))
		#----------------------------base 5-7------------------------------------------#
		pos = len(ZJoint57)-1
		print "-------",scalar[i][0],",", scalar[i][1],"\n", compJoint(ZJoint23[pos],ZJoint25[pos],ZJoint27[pos],ZJoint35[pos],ZJoint37[pos],ZJoint57[pos],p),"\n-------"
	print falsos
asd ()