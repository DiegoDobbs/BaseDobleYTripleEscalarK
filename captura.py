from callcryptolib import *
from Conversion_to_DBNS_Variable_with_restricted_exponents import *
from Conversion_to_TBNS_Variable_base import *
from Double_Base_2_3_Scalar_Multiplication_in_Odd_Characte import *
from Double_Base_2_5_Scalar_Multiplication_in_Odd_Characte import *
from Double_Base_2_7_Scalar_Multiplication_in_Odd_Characte import *
from Double_Base_3_5_Scalar_Multiplication_in_Odd_Characte import *
from Double_Base_3_7_Scalar_Multiplication_in_Odd_Characte import *
from Double_Base_5_7_Scalar_Multiplication_in_Odd_Characte import *
from Triple_base_2_3_5_multiplication_odd_character import *
from Triple_base_2_3_7_multiplication_odd_character import *
from Triple_base_2_5_7_multiplication_odd_character import *
from Triple_base_3_5_7_multiplication_odd_character import *
from Join_double_base_number_system_base import *
from Joint_Double_Base_2_3_Scalar_Multiplication import *
from Joint_Double_Base_2_5_Scalar_Multiplication import *
from Joint_Double_Base_2_7_Scalar_Multiplication import *
from Joint_Double_Base_3_5_Scalar_Multiplication import *
from Joint_Double_Base_3_7_Scalar_Multiplication import *
from Joint_Double_Base_5_7_Scalar_Multiplication import *


import random 
import numpy


def compDobleTriple(Z23,Z25,Z27,Z35,Z37,Z57,Z235,Z237,Z257,Z357,P):
	if affine(Z23,P)==affine(Z25,P)==affine(Z27,P)==affine(Z35,P)==affine(Z37,P)==affine(Z57,P)==affine(Z235,P)==affine(Z237,P)==affine(Z257,P)==affine(Z357,P):
		return True
	else :
		return False
def compJoint(ZJoint23,ZJoint25,ZJoint27,ZJoint35,ZJoint37,ZJoint57,P):
	if affine(ZJoint23,P)==affine(ZJoint25,P)==affine(ZJoint27,P)==affine(ZJoint35,P)==affine(ZJoint37,P)==affine(ZJoint57,P):
		return True
	else :
		return False

def main ():
	ti=time.time()
	for j in range (0,1):
		#escalares
		scalar = []
		#tiempo 
		tiempo23 = []
		tiempo25 = []
		tiempo27 = []
		tiempo35 = []
		tiempo37 = []
		tiempo57 = []
		tiempo235 = []
		tiempo237 = []
		tiempo257 = []
		tiempo357 = []	
		tiempoJoint23 = []
		tiempoJoint25 = []
		tiempoJoint27 = []
		tiempoJoint35 = []
		tiempoJoint37 = []
		tiempoJoint57 = []
		#resultados
		Z23 = []
		Z25 = []
		Z27 = []
		Z35 = []
		Z37 = []
		Z57 = []
		Z235 = []
		Z237 = []
		Z257 = []
		Z357 = []	
		ZJoint23 = []
		ZJoint25 = []
		ZJoint27 = []
		ZJoint35 = []
		ZJoint37 = []
		ZJoint57 = []
		#vectores de doble base
		s2 = [] 
		b2 = [] 
		t2 = [] 
		#vectores de triple base
		s3 = [] 
		b3 = [] 
		t3 = [] 
		d3 = [] 
		#vectores de joint 
		sb1 = []
		sb2 = []
		b2  = []
		c2  = []

		#variables 
		max = 10000#<===============================================================================================max
		timeAvg = []
		#define puntos 
		if j == 0:
			# puntos 
			p  = 115792089210356248762697446949407573530086143415290314195533631308867097853951	 #numero primo para 256-bits de nivel de seguridad NIST
			X1 = 23214596693397255141218547920536253619759004226613097475106265799817441198512  #Coordenadas de un punto P en la curva EC.
			Y1 = 17582485955261531990393572759413304059678227040548071610378634720965647717813
			Z1 = 1
			X2 = 98412530668235200848772828508190622194068156824181695326117330679756264623647
			Y2 = 50852179810991374232999932859585543263140189651850993040851792664262650594978
			Z2 = 1				
		elif j == 1: 
			p  = 6277101735386680763835789423207666416083908700390324961279	 #numero primo para 192-bits de nivel de seguridad NIST
			X1 = 3055563715971644849423804859220265481316585815874058627244 #Coordenadas de un punto P en la curva EC.
			Y1 = 5301271154980119921208363180474818072856515133833450622956
			Z1 = 1
			X2 = 3366172135749127752442661849960622274110712161924290025866 #Coordenadas de un punto P en la curva EC.
			Y2 = 6139723457849173165011744227944843453513622199649544688473
			Z2 = 1

		coor = {'x':X1,'y':Y1,'z':Z1}
		coor2 = {'x':X2,'y':Y2,'z':Z2}
		for i in range(0,max):
			tr0=time.time()
			print int(((i+1)*100)/max),"% ",i+1,"/",max,
			#define escalar ran es para calcualr cuando saco el escalar
			ran = True 
			while ran == True :
				aux  = int(random.uniform(57896044618658097711785492504343953926634992332820282019728792003956564819968, 115792089237316195423570985008687907853269984665640564039457584007913129639935))
				aux2 = int(random.uniform(57896044618658097711785492504343953926634992332820282019728792003956564819968, 115792089237316195423570985008687907853269984665640564039457584007913129639935))
				if aux not in scalar and aux2 not in scalar :
					scalar.append([aux,aux2])
					ran = False
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
			#----------------------------base 2-3----------------------------------------#
			#calcula los vectores
			#print " 2-3,",
			s2, b2, t2 = callDoble (2,3,scalar[i][0])
			v23  = {'s':s2,'b':b2,'t':t2}
			#calcula el la clave y o
			t0=time.time()
			Z23.append(ScalarMultiplicationInOdd23(v23,coor,p))
			t1=time.time()
			tiempo23.append((t1-t0))
			#----------------------------base 2-5----------------------------------------#
			#calcula los vectores
			#print "2-5,",
			s2, b2, t2 = callDoble (2,5,scalar[i][0])
			v25  = {'s':s2,'b':b2,'t':t2}
			#calcula el la clave y o
			t0=time.time()
			Z25.append(ScalarMultiplicationInOdd25(v25,coor,p))
			t1=time.time()
			tiempo25.append((t1-t0))
			#----------------------------base 2-7----------------------------------------#
			#calcula los vectores
			#print "2-7,",
			s2, b2, t2 = callDoble (2,7,scalar[i][0])
			v27  = {'s':s2,'b':b2,'t':t2}
			#calcula el la clave y o
			t0=time.time()
			Z27.append(ScalarMultiplicationInOdd27(v27,coor,p))
			t1=time.time()
			tiempo27.append((t1-t0))
			#----------------------------base 3-5----------------------------------------#
			#calcula los vectores
			#print "3-5,",
			s2, b2, t2 = callDoble (3,5,scalar[i][0])
			v35  = {'s':s2,'b':b2,'t':t2}
			#calcula el la clave y o
			t0=time.time()
			Z35.append(ScalarMultiplicationInOdd35(v35,coor,p))
			t1=time.time()
			tiempo35.append((t1-t0))
			#----------------------------base 3-7----------------------------------------#
			#calcula los vectores
			#print "3-7,",
			s2, b2, t2 = callDoble (3,7,scalar[i][0])
			v37  = {'s':s2,'b':b2,'t':t2}
			#calcula el la clave y o
			t0=time.time()
			Z37.append(ScalarMultiplicationInOdd37(v37,coor,p))
			t1=time.time()
			tiempo37.append((t1-t0))
			#----------------------------base 5-7----------------------------------------#
			#calcula los vectores
			#print "5-7,",
			s2, b2, t2 = callDoble (5,7,scalar[i][0])
			v57  = {'s':s2,'b':b2,'t':t2}
			#calcula el la clave y o
			t0=time.time()
			Z57.append(ScalarMultiplicationInOdd57(v57,coor,p))
			t1=time.time()
			tiempo57.append((t1-t0))
			#------------------------------base 3------------------------------------------#
			#----------------------------base 2-3-5----------------------------------------#
			#print "2-3-5,",
			s3, b3, t3, d3 =  calltiple (2,3,5,scalar[i][0])
			v235 = {'s':s3,'b':b3,'t':t3,'d':d3}
			t0=time.time()
			Z235.append(ScalarMultiplicationInOdd235(v235,coor,p))
			t1=time.time()
			tiempo235.append((t1-t0))
			#----------------------------base 2-3-7----------------------------------------#
			#print "2-3-7,",
			s3, b3, t3, d3 =  calltiple (2,3,7,scalar[i][0])
			v237 = {'s':s3,'b':b3,'t':t3,'d':d3}
			t0=time.time()
			Z237.append(ScalarMultiplicationInOdd237(v237,coor,p))
			t1=time.time()
			tiempo237.append((t1-t0))
			#----------------------------base 2-5-7----------------------------------------#
			#print "2-5-7,",
			s3, b3, t3, d3 =  calltiple (2,5,7,scalar[i][0])
			v257 = {'s':s3,'b':b3,'t':t3,'d':d3}
			t0=time.time()
			Z257.append(ScalarMultiplicationInOdd257(v257,coor,p))
			t1=time.time()
			tiempo257.append((t1-t0))
			#----------------------------base 3-5-7----------------------------------------#
			#print "3-5-7 ",
			s3, b3, t3, d3 =  calltiple (3,5,7,scalar[i][0])
			v357 = {'s':s3,'b':b3,'t':t3,'d':d3}
			t0=time.time()
			Z357.append(ScalarMultiplicationInOdd357(v357,coor,p))
			t1=time.time()
			tiempo357.append((t1-t0))
			#------------------------------joint-------------------------------------------#
			#----------------------------base 2-3------------------------------------------#
			#calcula los vectores
			#print " 2-3,",
			sb1, sb2, b2, c2 = JDBC(2,3,scalar[i][0],scalar[i][1])
			vD23  = {'s1':sb1,'s2':sb2,'b':b2,'t':c2}
			#calcula el la clave y o
			t0=time.time()
			ZJoint23.append(JointScalarMultiplication23(vD23,coor,coor2,p))
			t1=time.time()
			tiempoJoint23.append((t1-t0))
			#----------------------------base 2-5------------------------------------------#
			#calcula los vectores
			#print " 2-5,",
			sb1, sb2, b2, c2 = JDBC(2,5,scalar[i][0],scalar[i][1])
			vD25  = {'s1':sb1,'s2':sb2,'b':b2,'t':c2}
			#calcula el la clave y o
			t0=time.time()
			ZJoint25.append(JointScalarMultiplication25(vD25,coor,coor2,p))
			t1=time.time()
			tiempoJoint25.append((t1-t0))
			#----------------------------base 2-7------------------------------------------#
			#calcula los vectores
			#print " 2-7,",
			sb1, sb2, b2, c2 = JDBC(2,7,scalar[i][0],scalar[i][1])
			vD27  = {'s1':sb1,'s2':sb2,'b':b2,'t':c2}
			#calcula el la clave y o
			t0=time.time()
			ZJoint27.append(JointScalarMultiplication27(vD27,coor,coor2,p))
			t1=time.time()
			tiempoJoint27.append((t1-t0))
			#----------------------------base 3-5------------------------------------------#
			#calcula los vectores
			#print " 3-5,",
			sb1, sb2, b2, c2 = JDBC(3,5,scalar[i][0],scalar[i][1])
			vD35  = {'s1':sb1,'s2':sb2,'b':b2,'t':c2}
			#calcula el la clave y o
			t0=time.time()
			ZJoint35.append(JointScalarMultiplication35(vD35,coor,coor2,p))
			t1=time.time()
			tiempoJoint35.append((t1-t0))
			#----------------------------base 3-7------------------------------------------#
			#calcula los vectores
			#print " 3-7,",
			sb1, sb2, b2, c2 = JDBC(3,7,scalar[i][0],scalar[i][1])
			vD37  = {'s1':sb1,'s2':sb2,'b':b2,'t':c2}
			#calcula el la clave y o
			t0=time.time()
			ZJoint37.append(JointScalarMultiplication37(vD37,coor,coor2,p))
			t1=time.time()
			tiempoJoint37.append((t1-t0))
			#----------------------------base 5-7------------------------------------------#
			#calcula los vectores
			#print " 5-7,",
			sb1, sb2, b2, c2 = JDBC(5,7,scalar[i][0],scalar[i][1])
			vD57  = {'s1':sb1,'s2':sb2,'b':b2,'t':c2}
			#calcula el la clave y o
			t0=time.time()
			ZJoint57.append(JointScalarMultiplication57(vD57,coor,coor2,p))
			t1=time.time()
			tiempoJoint57.append((t1-t0))
			#------------------------------------------------------------------------------#
			tr1=time.time()
			pos = len(Z23)-1
			print "t:",(tr1-tr0),"sec.",compDobleTriple(Z23[pos],Z25[pos],Z27[pos],Z35[pos],Z37[pos],Z57[pos],Z235[pos],Z237[pos],Z257[pos],Z357[pos],p), compJoint(ZJoint23[pos],ZJoint25[pos],ZJoint27[pos],ZJoint35[pos],ZJoint37[pos],ZJoint57[pos],p)
			timeAvg.append((tr1-tr0))
#--------------------------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------#
	#impresion de tiempos
	f = open('datos', 'w')
	if j == 0 :
		print "clave 256-bits"
		f.write("clave 256-bits")
	elif j == 1 :
		print "clave 192-bits"
		f.write("clave 192-bits")
	#-------------------------------------------imprime en consola-------------------------------------------
	 #print "\t\t\t\t\t\tDoble base \t\t\t\t\t\t\t\t\tTriple base "
	 #print "Escalar","\tBase 2-3","\tBase 2-5","\tBase 2-7","\tBase 3-5","\tBase 3-7","\tBase 5-7","\tBase 2-3-5","\tBase 2-5-7","\tBase 3-5-7"
	 #for i in range (0, len(scalar)):
	 #	print scalar[i][0],"\t",tiempo23[i],"\t",tiempo25[i],"\t",tiempo27[i],"\t",tiempo35[i],"\t",tiempo37[i],"\t",tiempo57[i],"\t",tiempo235[i],"\t",tiempo257[i],"\t",tiempo357[i]
	#-------------------------------------------imprime en archivo-------------------------------------------
	f.write ("\t\t\t\tDoble base\t\t\t\tTriple base \n")
	f.write ("Escalar\tBase 2-3\tBase 2-5\tBase 2-7\tBase 3-5\tBase 3-7\tBase 5-7\tBase 2-3-5\tBase 2-3-7\tBase 2-5-7\tBase 3-5-7\n")
	for i in range (0, len(scalar)):
		f.write (str("%d \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f" % (scalar[i][0],tiempo23[i],tiempo25[i],tiempo27[i],tiempo35[i],tiempo37[i],tiempo57[i],tiempo235[i],tiempo237[i],tiempo257[i],tiempo357[i])))
		f.write ("\n")
	#========================== imprime en archivo varianza =======================================#
	avg23,avg25,avg27,avg35,avg37,avg57,avg235,avg237,avg257,avg357 = numpy.var(tiempo23),numpy.var(tiempo25),numpy.var(tiempo27),numpy.var(tiempo35),numpy.var(tiempo37),numpy.var(tiempo57),numpy.var(tiempo235),numpy.var(tiempo237),numpy.var(tiempo257),numpy.var(tiempo357)
	d = open('promedios', 'w')
	d.write ("Varianza\n")
	d.write ("\t\t\t\tDoble base\t\t\t\tTriple base \n")
	d.write ("Base 2-3\tBase 2-5\tBase 2-7\tBase 3-5\tBase 3-7\tBase 5-7\tBase 2-3-5\tBase 2-3-7\tBase 2-5-7\tBase 3-5-7\n")
	d.write (str("%f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f" % (avg23,avg25,avg27,avg35,avg37,avg57,avg235,avg237,avg257,avg357)))
	#========================== imprime en archivo desviacion estandar =======================================#
	avg23,avg25,avg27,avg35,avg37,avg57,avg235,avg237,avg257,avg357 = numpy.std(tiempo23),numpy.std(tiempo25),numpy.std(tiempo27),numpy.std(tiempo35),numpy.std(tiempo37),numpy.std(tiempo57),numpy.std(tiempo235),numpy.std(tiempo237),numpy.std(tiempo257),numpy.std(tiempo357)
	d.write ("\n\n")
	d.write ("Desviacion estandar\n")
	d.write ("\t\t\t\tDoble base\t\t\t\tTriple base \n")
	d.write ("Base 2-3\tBase 2-5\tBase 2-7\tBase 3-5\tBase 3-7\tBase 5-7\tBase 2-3-5\tBase 2-3-7\tBase 2-5-7\tBase 3-5-7\n")
	d.write (str("%f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f" % (avg23,avg25,avg27,avg35,avg37,avg57,avg235,avg237,avg257,avg357)))
	#print "--------------------------------------------------------------------------------------------------------------"
	avg23,avg25,avg27,avg35,avg37,avg57,avg235,avg237,avg257,avg357 = numpy.mean(tiempo23),numpy.mean(tiempo25),numpy.mean(tiempo27),numpy.mean(tiempo35),numpy.mean(tiempo37),numpy.mean(tiempo57),numpy.mean(tiempo235),numpy.mean(tiempo237),numpy.mean(tiempo257),numpy.mean(tiempo357)
	print "\t\tPromedios"
	print "\t\t\t\t\t\tDoble base \t\t\t\t\t\t\t\t\tTriple base "
	print "Base 2-3\tBase 2-5\tBase 2-7\tBase 3-5\tBase 3-7\tBase 5-7\tBase 2-3-5\tBase 2-3-7\tBase 2-5-7\tBase 3-5-7"
	print avg23,"\t",avg25,"\t",avg27,"\t",avg35,"\t",avg37,"\t",avg57,"\t",avg235,"\t",avg237,"\t",avg257,"\t",avg357
	#========================== imprime en archivo promedios =======================================#
	d.write ("\n\n")
	d.write ("Promedios\n")
	d.write ("\t\t\t\tDoble base\t\t\t\tTriple base \n")
	d.write ("Base 2-3\tBase 2-5\tBase 2-7\tBase 3-5\tBase 3-7\tBase 5-7\tBase 2-3-5\tBase 2-3-7\tBase 2-5-7\tBase 3-5-7\n")
	d.write (str("%f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f \t %f" % (avg23,avg25,avg27,avg35,avg37,avg57,avg235,avg237,avg257,avg357)))
	minimo = min([avg23,avg25,avg27,avg35,avg37,avg57,avg235,avg237,avg257,avg357])
	#--------------------------------------mejor total----------------------------------------------------------------------#
	print "\n"
	d.write ("\n")
	if minimo == avg23:
		print "El mejor algoritmo es el de base 2-3\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo es el de base 2-3\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg25:
		print "El mejor algoritmo es el de base 2-5\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo es el de base 2-5\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg27:
		print "El mejor algoritmo es el de base 2-7\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo es el de base 2-7\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg35:
		print "El mejor algoritmo es el de base 3-5\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo es el de base 3-5\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg37:
		print "El mejor algoritmo es el de base 3-7\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo es el de base 3-7\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg57:
		print "El mejor algoritmo es el de base 5-7\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo es el de base 5-7\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg235:
		print "El mejor algoritmo es el de base 2-3-5\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo es el de base 2-3-5\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg237:
		print "El mejor algoritmo es el de base 2-3-7\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo es el de base 2-3-7\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg257:
		print "El mejor algoritmo es el de base 2-5-7\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo es el de base 2-5-7\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg357:
		print "El mejor algoritmo es el de base 3-5-7\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo es el de base 3-5-7\n El promedio de su tiempo es de : %f" % minimo)
	#--------------------------------------mejor doble base----------------------------------------------------------------------#
	minimo = min([avg23,avg25,avg27,avg35,avg37,avg57])
	if minimo == avg23:
		print "El mejor algoritmo de doble base es el de base 2-3\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo de doble base es el de base 2-3\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg25:
		print "El mejor algoritmo de doble base es el de base 2-5\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo de doble base es el de base 2-5\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg27:
		print "El mejor algoritmo de doble base es el de base 2-7\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo de doble base es el de base 2-7\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg35:
		print "El mejor algoritmo de doble base es el de base 3-5\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo de doble base es el de base 3-5\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg37:
		print "El mejor algoritmo de doble base es el de base 3-7\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo de doble base es el de base 3-7\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg57:
		print "El mejor algoritmo de doble base es el de base 5-7\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo de doble base es el de base 5-7\n El promedio de su tiempo es de : %f" % minimo)
	#--------------------------------------mejor triple bae---------------------------------------------------------------------#
	minimo = min([avg235,avg237,avg257,avg357])
	if minimo == avg235:
		print "El mejor algoritmo de triple base es el de base 2-3-5\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo de triple base es el de base 2-3-5\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg237:
		print "El mejor algoritmo de triple base es el de base 2-3-7\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo de triple base es el de base 2-3-7\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg257:
		print "El mejor algoritmo de triple base es el de base 2-5-7\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo de triple base es el de base 2-5-7\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avg357:
		print "El mejor algoritmo de triple base es el de base 3-5-7\n El promedio de su tiempo es de :",minimo
		d.write ("\nEl mejor algoritmo de triple base es el de base 3-5-7\n El promedio de su tiempo es de : %f" % minimo)
	print "\n"

#-------------------------------------------Joint -------------------------------------------------------
	#-------------------------------------------imprime en archivo-------------------------------------------
	r = open('datos2', 'w')	
	if j == 0 :
		print "clave 256-bits"
		r.write("clave 256-bits")
	elif j == 1 :
		print "clave 192-bits"
		r.write("clave 192-bits")
	#-------------------------------------------imprime en consola-------------------------------------------
	 #print ("\t\t\t\tBase Conjunta\n")
	 #print ("Escalar\tEscalar\tBase 2-3\tBase 2-5\tBase 2-7\tBase 3-5\tBase 3-7\tBase 5-7\n")
	 #for i in range (0, len(scalar)):
	 #	print (str("%d \t %d \t %f \t %f \t %f \t %f \t %f \t %f \t" % (scalar[i][0],scalar[i][1],tiempoJoint23[i],tiempoJoint25[i],tiempoJoint27[i],tiempoJoint35[i],tiempoJoint37[i],tiempoJoint57[i])))
	#-------------------------------------------imprime en archivo-------------------------------------------
	r.write ("\t\tJoint Base\n")
	r.write ("Escalar\tEscalar\tBase 2-3\tBase 2-5\tBase 2-7\tBase 3-5\tBase 3-7\tBase 5-7\n")
	for i in range (0, len(scalar)):
		r.write (str("%d \t %d \t %f \t %f \t %f \t %f \t %f \t %f \t" % (scalar[i][0],scalar[i][1],tiempoJoint23[i],tiempoJoint25[i],tiempoJoint27[i],tiempoJoint35[i],tiempoJoint37[i],tiempoJoint57[i])))
		r.write ("\n")
	#========================== imprime en archivo varianza =======================================#
	p = open('promediosjoint', 'w')
	avgJ23,avgJ25,avgJ27,avgJ35,avgJ37,avgJ57= numpy.var(tiempoJoint23),numpy.var(tiempoJoint25),numpy.var(tiempoJoint27),numpy.var(tiempoJoint35),numpy.var(tiempoJoint37),numpy.var(tiempoJoint57)
	p.write ("Base Conjutna varianza\n")
	p.write ("Base 2-3\tBase 2-5\tBase 2-7\tBase 3-5\tBase 3-7\tBase 5-7\n")
	p.write (str("%f \t %f \t %f \t %f \t %f \t %f \t" % (avgJ23,avgJ25,avgJ27,avgJ35,avgJ37,avgJ57)))
	#========================== imprime en archivo desviacion estandar =======================================#
	avgJ23,avgJ25,avgJ27,avgJ35,avgJ37,avgJ57= numpy.std(tiempoJoint23),numpy.std(tiempoJoint25),numpy.std(tiempoJoint27),numpy.std(tiempoJoint35),numpy.std(tiempoJoint37),numpy.std(tiempoJoint57)
	p.write ("\n\n")
	p.write ("Base Conjutna deviacion estandar\n")
	p.write ("Base 2-3\tBase 2-5\tBase 2-7\tBase 3-5\tBase 3-7\tBase 5-7\n")
	p.write (str("%f \t %f \t %f \t %f \t %f \t %f \t" % (avgJ23,avgJ25,avgJ27,avgJ35,avgJ37,avgJ57)))
	#print "--------------------------------------------------------------------------------------------------------------"
	avgJ23,avgJ25,avgJ27,avgJ35,avgJ37,avgJ57= numpy.mean(tiempoJoint23),numpy.mean(tiempoJoint25),numpy.mean(tiempoJoint27),numpy.mean(tiempoJoint35),numpy.mean(tiempoJoint37),numpy.mean(tiempoJoint57)
	print "\t\tPromedios"
	print "Base conjunta \n"
	print "Base 2-3\tBase 2-5\tBase 2-7\tBase 3-5\tBase 3-7\tBase 5-7"
	print avgJ23,"\t",avgJ25,"\t",avgJ27,"\t",avgJ35,"\t",avgJ37,"\t",avgJ57
	#========================== imprime en archivo promedios =======================================#
	p.write ("\n\n")
	p.write ("Base Conjutna promedio\n")
	p.write ("Base 2-3\tBase 2-5\tBase 2-7\tBase 3-5\tBase 3-7\tBase 5-7\n")
	p.write (str("%f \t %f \t %f \t %f \t %f \t %f \t" % (avgJ23,avgJ25,avgJ27,avgJ35,avgJ37,avgJ57)))
	minimo = min([avgJ23,avgJ25,avgJ27,avgJ35,avgJ37,avgJ57])
	#--------------------------------------mejor total----------------------------------------------------------------------#	
	print "\n"
	p.write ("\n")
	if minimo == avgJ23:
		print "El mejor algoritmo de doble base conjunta es el de base 2-3\n El promedio de su tiempo es de :",minimo
		p.write ("\nEl mejor algoritmo de doble base conjunta es el de base 2-3\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avgJ25:
		print "El mejor algoritmo de doble base conjunta es el de base 2-5\n El promedio de su tiempo es de :",minimo
		p.write ("\nEl mejor algoritmo de doble base conjunta es el de base 2-5\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avgJ27:
		print "El mejor algoritmo de doble base conjunta es el de base 2-7\n El promedio de su tiempo es de :",minimo
		p.write ("\nEl mejor algoritmo de doble base conjunta es el de base 2-7\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avgJ35:
		print "El mejor algoritmo de doble base conjunta es el de base 3-5\n El promedio de su tiempo es de :",minimo
		p.write ("\nEl mejor algoritmo de doble base conjunta es el de base 3-5\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avgJ37:
		print "El mejor algoritmo de doble base conjunta es el de base 3-7\n El promedio de su tiempo es de :",minimo
		p.write ("\nEl mejor algoritmo de doble base conjunta es el de base 3-7\n El promedio de su tiempo es de : %f" % minimo)
	elif minimo == avgJ57:
		print "El mejor algoritmo de doble base conjunta es el de base 5-7\n El promedio de su tiempo es de :",minimo
		p.write ("\nEl mejor algoritmo de doble base conjunta es el de base 5-7\n El promedio de su tiempo es de : %f" % minimo)

	tf=time.time()
	print "==============================================="
	print "El tiempo promedio de ejecucion de los metodos fue de ",numpy.mean([avg23,avg25,avg27,avg35,avg37,avg57,avg235,avg237,avg257,avg357,avgJ23,avgJ25,avgJ27,avgJ35,avgJ37,avgJ57])
	print "El tiempo promedio por ciclo fue de ",numpy.mean(timeAvg)
	print "Tiempo de ejecucion: ",
	if (tf-ti) > 86400: #dias 
		print int(round((tf-ti)/86400)),"dias.",
	timeHours=(tf-ti)%86400
	if timeHours > 3600: #horas 
		print int(round(timeHours/3600)),"horas.",
	timeMinutes=timeHours%3600
	if timeMinutes > 60: #minutos 
		print int(round(timeMinutes/60)),"minutos.",
	timeSeconds=timeMinutes%60
	if timeSeconds > 0: #segundos 
		timeSeconds=timeSeconds%60
		print int(round(timeSeconds)),"segundos."

main()