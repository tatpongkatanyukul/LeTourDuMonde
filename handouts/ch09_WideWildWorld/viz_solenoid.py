import numpy as np
from matplotlib import pyplot as plt
from P11 import Solenoid

from math import pi

def unitvec(Fx, Fy, Fz):
    '''
    F: field in shape (nx, ny, nz)
    '''

    Fmag = np.sqrt(Fx**2 + Fy**2 + Fz**2)
    Ux = Fx/Fmag
    Uy = Fy/Fmag
    Uz = Fz/Fmag

    return Ux, Uy, Uz, Fmag


def sol_viz(Xs, Ys, Zs, R, CurrentI, mu0, Nturns, lengthL):
    '''
    Assuming Xs, Ys, Zs must be uniformly distributed.
    We use ```imshow```, so it arranges result pixel by pixel,
    so it has to be uniformly distributed (better with the same resoltion on all x, y, z.) 
    '''

    # Instantiate Solenoid
    print('Instantiate a solenoid.')
    s = Solenoid(R, CurrentI, mu0, Nturns, lengthL)

    # Compute B
    print('Compuate a magnetic field. It may take a while...')
    Bx, By, Bz = s.compute_B(Xs, Ys, Zs, N=100)
    uBx, uBy, uBz, magB = unitvec(Bx, By, Bz)    

    #########################
    # Perform graphics
    #########################

    # Scale coordinate to plot frame
    # * Logical y in [min(Ys), max(Ys)]
    # * Plot y in [0, len(Ys)-1] (resulting from imshow)

    # We fix x = 0 here!

    yl = 0 
    yp = (yl - np.min(Ys))/(np.max(Ys) - np.min(Ys)) * (len(Ys)-1) + 0
    zl = s.Zs
    Zp = (zl - np.min(Zs))/(np.max(Zs) - np.min(Zs)) * (len(Zs)-1) + 0

    Rl1 = -R
    Rp1 = (Rl1 - np.min(Ys))/(np.max(Ys) - np.min(Ys)) * (len(Ys)-1) + 0

    Rl2 = R
    Rp2 = (Rl2 - np.min(Ys))/(np.max(Ys) - np.min(Ys)) * (len(Ys)-1) + 0

    # Run the plots
    fig, ax = plt.subplots(1, 2)
    # fig.tight_layout(rect=[0.1, 0.1, 2, 2], h_pad=4, w_pad=4)
    # tight_layout somehows does not work well outside jupyter notebook.

    # Caution: imshow reverse y-axis
    # So, pay A LOT OF ATTENTION on the y-axis.

    # x = Xs[i]
    i = 0
    plt.subplot(1,2,1)
    im = plt.imshow(magB[i,:,::-1].T, cmap = 'Reds' , interpolation = 'nearest' )
    plt.title('Magnetic field (at x= {:.1f}): unit vector'.format(Xs[i]))
    plt.xlabel('y')
    plt.ylabel('z')
    
    m = 5
    ax[0].set_xticks(list(range(len(Ys)))[::m])             # Tick every m points
    ax[0].set_xticklabels(["{:.4f}".format(y) for y in Ys[::m]])
    ax[0].set_yticks(list(range(len(Zs)))[::m])             # Tick every m points
    ax[0].set_yticklabels(["{:.4f}".format(z) for z in Zs[::-1][::m]])
    ax[0].set_aspect( 1 )

    # plt.colorbar(im)
    plt.quiver(uBy[i,:,::-1].T, uBz[i,:,::-1].T)

    markL = '.'
    markR = 'x'
    if CurrentI < 0:
        markR = 'x'
        markL = '.'

    plt.plot(np.array([ Rp1 ]*s.N), len(Zs) - 1 - Zp, 'y'+markL)
    plt.plot(np.array([ Rp2 ]*s.N), len(Zs) - 1 - Zp, 'y'+markR)

    plt.subplot(1,2,2)
    im = plt.imshow(magB[i,:,::-1].T, cmap = 'Reds' , interpolation = 'nearest' )
    plt.title('Magnetic field (at x= {:.1f}): vector with magnitude'.format(Xs[i]))
    plt.xlabel('y')
    plt.ylabel('z')

    ax[1].set_xticks(list(range(len(Ys)))[::m])             # Tick every m points
    ax[1].set_xticklabels(["{:.4f}".format(y) for y in Ys[::m]])
    ax[1].set_yticks(list(range(len(Zs)))[::m])             # Tick every m points
    ax[1].set_yticklabels(["{:.4f}".format(z) for z in Zs[::-1][::m]])
    ax[1].set_aspect( 1 )

    # plt.colorbar(im)
    plt.quiver(By[i,:,::-1].T, Bz[i,:,::-1].T)

    markL = '.'
    markR = 'x'
    if CurrentI < 0:
        markR = 'x'
        markL = '.'

    plt.plot(np.array([ Rp1 ]*s.N), len(Zs) - 1 - Zp, 'y'+markL)
    plt.plot(np.array([ Rp2 ]*s.N), len(Zs) - 1 - Zp, 'y'+markR)

    plt.show()    


# end def sol_viz


if __name__ == '__main__':

    # Define the system
    mu0 = 4e-7 * pi
    res = 0.00006
    R = 0.0004
    CurrentI = 3
    Nturns = 20
    lengthL = 0.0005

    # Point of interest
    Xs = np.arange(0, res, res)
    Ys = np.arange(-R*1.5, R*3, res)
    Zs = np.arange(-R*0.5, R*2, res)

    # Run visualization
    sol_viz(Xs, Ys, Zs, R, CurrentI, mu0, Nturns, lengthL)

