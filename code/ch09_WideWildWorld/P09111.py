import numpy as np
from math import sqrt, pi, sin, cos

def integrate_n(fx, xa, xb, n):
    '''
    Numerical integration with midpoint rule.
    fx: a function to be integrated.
    xa: an initial point of integration.
    xb: a final point of integration.
    n: a number of subintevals.
    '''

    dx = (xb - xa)/n

    # lower end of the subinterval
    sl = xa
    Mn = 0
    for i in range(n):
        mi = sl + dx/2
        Mn += fx(mi) * dx

        # Prep sl for the next subinterval 
        sl = sl + dx
    # end for i
    return Mn


def dB(Point, LoopR, LoopI, mu0, theta):
    '''
    Point: a coordinate of a point of interest in tuple (x, y, z).
    LoopR: a radius of the loop.
    LoopI: a current flowing in the loop: I > 0 ccw from top view and vice versa.
    mu0: permeability of free space
    Use math function from ```math``` library. It will be graded without numpy.
    '''
    x, y, z = Point
    R = LoopR

    K = mu0 * LoopI/(4 * pi)
    r = lambda theta: sqrt( (x - R*cos(theta))**2 + \
                                 (y - R*sin(theta))**2 + \
                                 z**2)
    dBx = lambda theta: K/r(theta)**3 * R*z*cos(theta)
    dBy = lambda theta: K/r(theta)**3 * R*z*sin(theta)
    dBz = lambda theta: -K/r(theta)**3 * R*(sin(theta)*(y - R*sin(theta)) + \
                                            cos(theta)*(x - R*cos(theta)))

    return dBx(theta), dBy(theta), dBz(theta)


def BVec(Point, LoopR, LoopI, mu0, N=1000):
    '''
    Point: a coordinate of a point of interest in tuple (x, y, z).
    LoopR: a radius of the loop.
    LoopI: a current flowing in the loop: I > 0 ccw from top view and vice versa.
    mu0: permeability of free space
    N: meta-parameter of numerical integration: a number of subintervals
    Use math function from ```math``` library. It will be graded without numpy.

    Call dB and numerical integration so that it can be checked in smaller steps.
    '''

    x, y, z = Point
    R = LoopR

    K = mu0 * LoopI/(4 * pi)
    r = lambda theta: sqrt( (x - R*cos(theta))**2 + \
                                 (y - R*sin(theta))**2 + \
                                 z**2)
    dBx = lambda theta: K/r(theta)**3 * R*z*cos(theta)
    dBy = lambda theta: K/r(theta)**3 * R*z*sin(theta)
    dBz = lambda theta: -K/r(theta)**3 * R*(sin(theta)*(y - R*sin(theta)) + \
                                            cos(theta)*(x - R*cos(theta)))

    # Integrate dB
    Bx = integrate_n(dBx, 0, 2*pi, N)
    By = integrate_n(dBy, 0, 2*pi, N)    
    Bz = integrate_n(dBz, 0, 2*pi, N)

    return Bx, By, Bz


class CurrentLoop:
    '''
    Current loop whose center is at (0, 0, z) with radius R and current I.
    Direction of current I:
    I > 0 means counter-clockwise looking from +z.
    I < 0 means clockwise looking from +z. 
    '''
    def __init__(self, z, R, I, mu0):
        self.z = z
        self.R = R
        self.I = I
        self.mu0 = mu0

    def compute_B(self, X, Y, Z, N=1000):
        '''
        X: field range along x-axis
        Y: field range along y-axis
        Z: field range along z-axis
        '''
        # Since the loop is at self.z off the origin (0,0,0),
        # we need to offset this on Z.
        Zp = np.array(Z) - self.z

        Bx = np.zeros((len(X), len(Y), len(Zp)))
        By = np.zeros((len(X), len(Y), len(Zp)))
        Bz = np.zeros((len(X), len(Y), len(Zp)))

        # Compute each B at each point in volume X . Y . Zp
        for i, x in enumerate(X):
            for j, y in enumerate(Y):
                for k, z in enumerate(Zp):
                    Bx[i,j,k], By[i,j,k], Bz[i,j,k] = \
                    BVec((x,y,z), self.R, self.I, self.mu0, N)
                # end for k
            # end for i
        #end for j  

        return Bx, By, Bz
    # end def


class Solenoid:
    def __init__(self, radiusR, currentI, mu0, numTurnsN, lengthL):
        '''
        Solenoid location center at (0,0) whose ends are at z=0 and z=L.
        Approximate a magnetic field of solenoid of N turns by N current loops.

            B_total = sum_n B_n
        where B_n is a magnetic field caused by the nth current loop.        
        Current loops are assumed to be evenly align along z-axis from z=0 to z=L.
        '''

        self.R = radiusR
        self.I = currentI
        self.mu0 = mu0
        self.N = numTurnsN
        self.L = lengthL

        self.Zs = []    # all current loop locations along z-axis
        z_step = self.L/(self.N - 1)
        z = 0
        for i in range(self.N):
            self.Zs.append(z)
            z += z_step
        # end for i

    def compute_B(self, X, Y, Z, N=1000):

        # Total B
        BTx = 0
        BTy = 0
        BTz = 0

        for i in range(self.N):
            # Define current loops.
            cl = CurrentLoop(self.Zs[i], self.R, self.I, self.mu0)
            
            # Compute B
            Bx, By, Bz = cl.compute_B(X, Y, Z, N)

            BTx += Bx
            BTy += By
            BTz += Bz
            
        # end for i

        return BTx, BTy, BTz
    # end def
# end class


if __name__ == '__main__':
    mu0 = 4e-7 * pi
    R = 0.008
    CurrentI = 0.8
    Nturns = 20
    lengthL = 0.025
    Ys = [0, 0.04]

    s = Solenoid(R, CurrentI, mu0, Nturns, lengthL)

    N = 100
    Bx, By, Bz = s.compute_B([0], Ys, [lengthL/2], N)

    for i, y in enumerate(Ys):
        print('B(0,{},L/2) = [ {:.4f} ; {:.4f} ; {:.4f} ]x10^-6'.format(y, 
                              Bx[0,i,0]*1e6, By[0,i,0]*1e6, Bz[0,i,0]*1e6)) 