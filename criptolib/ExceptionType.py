
def checktype (a,p):
	if type(a)==dict and len(a)==3 and type(a['x'])==long and type(a['y'])==long and(type(a['z'])==long or type(a['z'])==int)and type(p)==long:
		return True
	else :
		if type(a)!=dict:
			raise Exception('Must be type dictionary')
		elif len(a)!=3:
			raise Exception('The list must be size 3')
		elif type(a['x'])!=long or type(a['y'])!=long or (type(a['z'])!=long and type(a['z'])!=int):
			raise Exception('All three elements of the list must be long type ')
		elif type(p)!= long  :
			raise Exception('Number p must be a int')
		else :
			raise Exception('U destroy all good and pretty in this planet')
