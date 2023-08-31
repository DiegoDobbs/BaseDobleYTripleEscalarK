from ExceptionType import *
from affine import *

#FAST QUINTUPLING
def Quintupling(coor,P):
    checktype(coor,P)

    X1 = coor['x']
    Y1 = coor['y']
    Z1 = coor['z']
    a  = -3
    #alpha = (3*(X1+pow(Z1,2))*(X1-pow(Z1,2)))%P
    #X11   = (4*X1*pow(Y1,2))%P
    alpha = (3*pow(X1,2)+a*pow(Z1,4))%P
    X11   = (2*(pow((X1+pow(Y1,2)),2)-pow(X1,2)-pow(Y1,4)))%P
    Y11   = (16*pow(Y1,4))%P
    X2    = (pow(alpha,2)-2*X11)%P
    theta = (X11-X2)%P
    Y2    = (pow((alpha+theta),2)-pow(alpha,2)-pow(theta,2)-Y11)%P
    Z2    = (pow((Y1+Z1),2)-pow(Y1,2)-pow(Z1,2))%P
    omega = (Y11-Y2)%P
    X21   = (4*X2*pow(theta,2))%P
    Y21   = (4*Y2*pow(theta,3))%P
    phi   = (pow(omega,2)-4*pow(theta,3)-3*X21)%P
    gamma = (pow(omega,2)+pow(phi,2)-pow((omega+phi),2)-4*Y21)%P
    
    X5 = (pow(gamma,2)-4*pow(phi,3)-8*X21*pow(phi,2))%P
    Y5 = (gamma*(4*X21*pow(phi,2)-X5)-8*Y21*pow(phi,3))%P
    Z5 = (2*Z2*(pow((theta+phi),2)-pow(theta,2)-pow(phi,2)))%P

    return {'x':X5,'y':Y5,'z':Z5}



def NormalQuintupling(coor,P):
    checktype(coor,P)

    X1 = coor['x']
    Y1 = coor['y']
    Z1 = coor['z']

    beta  = (16*pow(Y1,4))%P
    theta = (3*(X1+pow(Z1,2))*(X1-pow(Z1,2)))%P
    omega = (12*X1*pow(Y1,2)-pow(theta,2))%P
    alpha = (pow((theta+omega),2)-(pow(theta,2)+pow(omega,2)+beta))%P
    gamma = (alpha*beta-pow(omega,3))%P
    phi   = (gamma-pow(alpha,2))%P
    rho   = (2*(pow((pow(Y1,2)+alpha),2)-pow(Y1,4)-pow(alpha,2)))%P
    varphi = (omega*phi)%P

    X5 = (4*(X1*pow(gamma,2)-rho*varphi))%P
    Y5 = (8*Y1*(gamma*pow(omega,3)*(3*pow(alpha,2)-gamma)-pow(alpha,4)*(pow(omega,3)+alpha*beta)))%P
    Z5 = (pow((Z1+gamma),2)-pow(Z1,2)-pow(gamma,2))%P

    return {'x':X5,'y':Y5,'z':Z5}


def Quintupling_affine(coor,p):
    coor=affine(Quintupling(coor,p),p)
    return(coor)

def Quintupling_affiner(coor,p):
    coor=affiner(Quintupling(coor,p),p)
    return(coor)

#P  = 6277101735386680763835789423207666416083908700390324961279
#X1 = 3055563715971644849423804859220265481316585815874058627244#coor['x']#
#Y1 = 5301271154980119921208363180474818072856515133833450622956#coor['y']#
#Z1 = 1#coor['z']#

#print affine(Quintupling({'x':X1,'y':Y1,'z':Z1},P),P)
#print affine(FastQuintupling({'x':X1,'y':Y1,'z':Z1},P),P)
#print "5P", Quintupling_affine({'x':X1,'y':Y1,'z':Z1},P)
#print "25 P", affine(Quintupling(Quintupling({'x':X1,'y':Y1,'z':Z1},P),P),P)
#print "125 P", affine(Quintupling(Quintupling(Quintupling({'x':X1,'y':Y1,'z':Z1},P),P),P),P)
#print "625 P", affine(Quintupling(Quintupling(Quintupling(Quintupling({'x':X1,'y':Y1,'z':Z1},P),P),P),P),P)
#print "3125 P", affine(Quintupling(Quintupling(Quintupling(Quintupling(Quintupling({'x':X1,'y':Y1,'z':Z1},P),P),P),P),P),P)
#print "15625 P", affine(Quintupling(Quintupling(Quintupling(Quintupling(Quintupling(Quintupling({'x':X1,'y':Y1,'z':Z1},P),P),P),P),P),P),P)

#
# New Multibase Non-Adjacent Form Scalar Multiplication and its Application to Elliptic Curve Cryptosystems
#(extended version) Patrick Longa, and Ali Miri
# appendix c page 35
#