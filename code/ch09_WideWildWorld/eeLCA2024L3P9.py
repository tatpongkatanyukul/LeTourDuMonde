import math

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


if __name__ == '__main__':
    # Test 1: f1(x) = x^3
    def f1(x):
        return x**3

    r = integrate_n(f1, 0, 1, 1000)
    print('integral of f1 from 0 to 1 (with n = 1000) =', r)

    # Test 2: f2(x) = sin(x)
    def f2(x):
        return math.sin(x)

    r = integrate_n(f2, 0, math.pi, 100)
    print('integral of f2 from 0 to pi (with n = 100) =', r)