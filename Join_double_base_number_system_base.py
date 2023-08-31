
b1 = 0
b2 = 0
	
def totaal(n,m,c,d,a,b):
	total1 = 0
	total2 = 0
	for i in range (0,len(c)):
		aux = pow(b1,a[i])*pow(b2,b[i])
		total1 = total1 + c[i]*aux
		total2 = total2 + d[i]*aux
	print( "n =",n,"\nm =",m)
	for i in range (0,len(c)):
		if i == 0 :
			print( "[",total1,"|",total2,"]","=",)
		print( "(",c[i],d[i],")","*","(",b1,"^",a[i],"*",b2,"^",b[i],")",)
		if i != len(c)-1 :
			print( " + ",)
	print( )
	if n-total1 == 0 :
		print( "N bien")
	else :
		print( "N mal",n-total1)
	if m-total2 == 0 :
		print( "M bien")
	else :
		print( "M mal",m-total2)

def vb1(a):
	i=0
	while a%b1 == 0 and a != 0:
		i = i+1
		a = a/b1
	return i

def vb2(a):
	i=0
	while a%b2 == 0 and a != 0 :
		i = i+1
		a = a/b2 
	return i

def doble_vb1(n,m):
	return min([vb1(n),vb1(m)])

def doble_vb2(n,m):
	return min([vb2(n),vb2(m)])

def gain(x,y):
	best = []
	prob = [-1,0,1]
	for d in prob:
		for c in prob:
			exp2 = doble_vb1(x-c,y-d)
			exp3 = doble_vb2(x-c,y-d)
			total = pow(b1,exp2)*pow(b2,exp3)
			best.append([total,c,d])
	#print("=====", best)
	aux = max(best)
	#print( aux,"=====")
	#print( "(",aux[1],",",aux[2],")",)
	return aux[0],aux[1],aux[2]#g,c,d

def JDBC(base1,base2,n,m,pri=False):
	global b1
	global b2
	b1 = base1
	b2 = base2 
	i = 0
	g = 0 
	a = []
	b = []
	c = []
	d = []
	a.append(doble_vb1(n,m))
	b.append(doble_vb2(n,m))
	x = n/(pow(b1,a[0])*pow(b2,b[0]))
	y = m/(pow(b1,a[0])*pow(b2,b[0]))
	while x > 1 or y > 1 :
		#print( "x,y",x,y,"//",)
		g,cAux,dAux = gain(x,y)
		if x == 0 and y > 1 :
			c.append(0)
		else : 
			c.append(int(cAux))
		if y == 0 and x > 1 :
			d.append(0)
		else : 
			d.append(int(dAux))
		i = i+1
		x = (x-c[i-1])/g
		y = (y-d[i-1])/g
		a.append(a[i-1]+vb1(g))
		b.append(b[i-1]+vb2(g))
	c.append(x)
	d.append(y)
	#ordena arreglos 
	c.reverse()
	d.reverse()
	a.reverse()
	b.reverse()
	if pri == False :
		#print( "c",c)
		#print( "d",d)
		return c,d,a,b
	else :
		print( "\n")
		print( "c s1:=",c,";")
		print( "d s2:=",d,";")
		print( "a b:=",a,";")
		print( "b t:=",b,";")
		totaal(n,m,c,d,a,b)

#JDBC(5,7,105,105,True)
#JDBC(2,3,99350856800467538618999269768037654229007266165117836980132092741325055590400, 111974479055683106585023703159973846416171258859984835903968985555777974435840,True )

