def totaal(n,m,c,d,a,b):
	total1 = 0
	total2 = 0
	for i in range (0,len(c)):
		aux = pow(2,a[i])*pow(3,b[i])
		total1 = total1 + c[i]*aux
		total2 = total2 + d[i]*aux
	print "n =",n,"\nm =",m
	if n-total1 == 0 :
		print "N bien"
	else :
		print "N mal",n-total1
	if m-total2 == 0 :
		print "M bien"
	else :
		print "M mal",m-total2
		
def v2(a):
	i=0
	while a%2 == 0 and a != 0:
		i = i+1
		a = a/2
	return i

def v3(a):
	i=0
	while a%3 == 0 and a != 0 :
		i = i+1
		a = a/3 
	return i

def doble_v2(n,m):
	return min([v2(n),v2(m)])

def doble_v3(n,m):
	return min([v3(n),v3(m)])

def gain(x,y):
	best = []
	prob = [-1,0,1]
	for d in prob:
		for c in prob:
			exp2 = doble_v2(x-c,y-d)
			exp3 = doble_v3(x-c,y-d)
			total = pow(2,exp2)*pow(3,exp3)
			best.append([total,c,d])
	aux = max(best)
	return aux[0],aux[1],aux[2]#g,c,d

def JDBC(n,m):
	i = 0
	g = 0 
	a = []
	b = []
	c = []
	d = []
	a.append(doble_v2(n,m))
	b.append(doble_v3(n,m))
	x = n/(pow(2,a[0])*pow(3,b[0]))
	y = m/(pow(2,a[0])*pow(3,b[0]))
	while x > 1 or y > 1 :
		g,cAux,dAux = gain(x,y)
		c.append(int(cAux))
		d.append(int(dAux))
		i = i+1
		x = (x-c[i-1])/g
		y = (y-d[i-1])/g
		a.append(a[i-1]+v2(g))
		b.append(b[i-1]+v3(g))
	c.append(x)
	d.append(y)
	#ordena arreglos 
	c.reverse()
	d.reverse()
	a.reverse()
	b.reverse()
	print "c",c
	print "d",d
	print "a",a
	print "b",b
	totaal(n,m,c,d,a,b)

JDBC(29,177)
#JDBC(57896044618658097711785492504343953926634992332820282019728792003956564819968,115792089237316195423570985008687907853269984665640564039457584007913129639935)

