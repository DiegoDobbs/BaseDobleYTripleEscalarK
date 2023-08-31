from modinvAndEgcd import *

def affine(coor,p):
	X3 = coor['x']*(modinv(pow(coor['z'],2),p))%p
  	Y3 = coor['y']*(modinv(pow(coor['z'],3),p))%p 
  	Z3 = coor['z']/coor['z']
  	return {'x':X3,'y':Y3,'z':Z3}

def affiner(coor,p):
	X3 = coor['x']*(modinvr(pow(coor['z'],2),p))%p
  	Y3 = coor['y']*(modinvr(pow(coor['z'],3),p))%p 
  	Z3 = coor['z']/coor['z']
  	return {'x':X3,'y':Y3,'z':Z3}