from ExceptionType import *
from affine import *


#FastTripling
def ThreeJacobian(coor,P):
    checktype(coor,P)    
    #asiganacion de valores
    #P = 6277101735386680763835789423207666416083908700390324961279
    X1 = coor['x']#3055563715971644849423804859220265481316585815874058627244
    Y1 = coor['y']#5301271154980119921208363180474818072856515133833450622956
    Z1 = coor['z']#1
    
    theta = (3*(X1+pow(Z1,2))*(X1-pow(Z1,2)))%P
    omega = (12*X1*pow(Y1,2)-pow(theta,2))%P
    alpha = (pow((theta+omega),2)-pow(theta,2)-pow(omega,2))%P
    beta  = (16*pow(Y1,4))%P

    X3 = (16*pow(Y1,2)*(beta-alpha)+4*X1*pow(omega,2))%P
    Y3 = (8*Y1*((alpha-beta)*(2*beta-alpha)-pow(omega,3)))%P
    Z3 = (pow((Z1+omega),2)-pow(Z1,2)-pow(omega,2))%P

    return {'x':X3,'y':Y3,'z':Z3}

def tripling(coor,P):
    checktype(coor,P)    
    #asiganacion de valores
    #P = 6277101735386680763835789423207666416083908700390324961279
    X1 = coor['x']#3055563715971644849423804859220265481316585815874058627244
    Y1 = coor['y']#5301271154980119921208363180474818072856515133833450622956
    Z1 = coor['z']#1
    X3 = 0
    Y3 = 0
    Z3 = 0    
    #calculo Beta
    BETA   = (8*pow(Y1,4))%P
    #print "BETA  = ",BETA
    #fin beta
    #calculo theta
    THETA  = (3*pow(X1,2)+(-3)*pow(Z1,4))%P
    #print"THETA = ",THETA
    #fin theta
    #calculo omega
    OMEGA  = (12*X1*pow(Y1,2)-pow(THETA,2))%P
    #print"OMEGA = ",OMEGA
    #fin omega
    #calculo alfa
    ALFA   = (THETA*OMEGA)%P
    #print "ALFA = ",ALFA
    #fin alfa
    #calculo x3
    X3  = (8*pow(Y1,2)*(BETA-ALFA)+X1*pow(OMEGA,2))%P
    #print "X3 = ", X3
    #fin x3
    #calculo y3
    Y3  = (Y1*(4*(ALFA-BETA)*(2*BETA-ALFA)-pow(OMEGA,3)))%P
    #print "Y3 = ",Y3
    #fin y3
    #calculo z3
    Z3  = (Z1*OMEGA)%P
    #print"Z3 = ", Z3
    #fin z3
    return {'x':X3,'y':Y3,'z':Z3}

def ThreeJacobian_affine(coor,p):
    coor=affine(ThreeJacobian(coor,p),p)
    return(coor)

def ThreeJacobian_affiner(coor,p):
    coor=affiner(ThreeJacobian(coor,p),p)
    return(coor)




#P  = 6277101735386680763835789423207666416083908700390324961279
#X1 = 3055563715971644849423804859220265481316585815874058627244#coor['x']#
#Y1 = 5301271154980119921208363180474818072856515133833450622956#coor['y']#
#Z1 = 1#coor['z']#
    
#print "3 P",ThreeJacobian_affiner({'x':X1,'y':Y1,'z':Z1},P)
#print "9 p", affine(ThreeJacobian(ThreeJacobian({'x':X1,'y':Y1,'z':Z1},P),P),P)
#print "27 p", affine(ThreeJacobian(ThreeJacobian(ThreeJacobian({'x':X1,'y':Y1,'z':Z1},P),P),P),P)
#print "81 p",affine(ThreeJacobian(ThreeJacobian(ThreeJacobian(ThreeJacobian({'x':X1,'y':Y1,'z':Z1},P),P),P),P),P)
#print "243 p",affine(ThreeJacobian(ThreeJacobian(ThreeJacobian(ThreeJacobian(ThreeJacobian({'x':X1,'y':Y1,'z':Z1},P),P),P),P),P),P)