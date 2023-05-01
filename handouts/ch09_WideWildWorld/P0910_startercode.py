from math import sin, cos, pi, sqrt

def integrate_n(fx, xa, xb, n):
    '''
    Numerical integration with midpoint rule.
    fx: a function to be integrated.
    xa: an initial point of integration.
    xb: a final point of integration.
    n: a number of subintevals.
    '''
    Mn = 0
    # Dummy code

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

    Kr = mu0 * LoopI/(4 * pi)
    r = lambda theta: sqrt( (x - R*cos(theta))**2 + \
                                 (y - R*sin(theta))**2 + \
                                 z**2)

    dBx = lambda theta: Kr/r(theta)**3 * R*z*cos(theta)
    dBy = lambda theta: 0 # Dummy code
    dBz = lambda theta: 0 # Dummy code

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

    # Dummy code

    dBx = lambda theta: 0 # Dummy
    dBy = lambda theta: 0 # Dummy
    dBz = lambda theta: 0 # Dummy

    # Integrate dB
    Bx = integrate_n(dBx, 0, 2*pi, N)
    By = 0 # Dummy
    Bz = 0 # Dummy

    return Bx, By, Bz


if __name__ == '__main__':
    # Test dB
    P = (0, 0, 10)
    R = 0.02
    I = 0.3
    mu0 = 4e-7 * pi
    for t in [0, pi/4, pi/2, 3*pi/4, pi, 5*pi/4, 3*pi/2, 7*pi/4]:
        dBx, dBy, dBz = dB(P, R, I, mu0, t)
        print('Theta: {:.2f} rad; dB = ( {:.4f} |x> + {:.4f} |y> + {:.4f} |z> ) x 10^-11'.format(t, dBx*1e11, dBy*1e11, dBz*1e11))

    # Test Bvec
    zs = [-0.2, -0.1, 0.0, 0.1, 0.2]
    for i, z in enumerate(zs):
        Point = (0, 0, z)
        Bx, By, Bz = BVec(Point, R, I, mu0, 1000)
        print('z = {}; B = ( {:.4f} x 10^-22|x> + {:.4f} x 10^-22|y> + {:.4f} x 10^-9|z> ) '.format(z, Bx*1e22, By*1e22, Bz*1e9))
