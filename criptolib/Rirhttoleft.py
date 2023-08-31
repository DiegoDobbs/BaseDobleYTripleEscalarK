
def RtoL(a,base):
	if base <= 10:
		raise Exception('The base must be < 10')
		
	cero= 1
	bin = 0
	zero = 0
	x = a
	a = 0
	#print " base = ",base
	#print "x   = ",x
	q = x / base
	a=x-(q*base)
	if(a==0):
		cero=cero*10

	while (q>zero):
		if(q==zero):
			break;
		q = x/base
		x = q
		q = x/base
		aux2=x-(q*base)
		a=a*10
		a=a+aux2
		if(a==zero):
			cero=cero*10

	while(a!=zero):
		aux2=a%10
		a=a/10
		bin=bin*10
		bin=bin+aux2

	bin=bin*cero
	#print"bin = ",bin
	return bin