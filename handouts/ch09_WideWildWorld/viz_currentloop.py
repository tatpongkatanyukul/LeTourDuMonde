import numpy as np
from matplotlib import pyplot as plt
from math import pi

from P10 import dB, BVec


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


def unitvec(Fx, Fy, Fz):
    '''
    F: field in shape (nx, ny, nz)
    '''

    Fmag = np.sqrt(Fx**2 + Fy**2 + Fz**2)
    Ux = Fx/Fmag
    Uy = Fy/Fmag
    Uz = Fz/Fmag

    return Ux, Uy, Uz, Fmag



def cl_viz(Xs, Ys, Zs, mu0, R, I):
    '''
    Assuming Xs, Ys, Zs are uniformly distributed.
    '''

    # Instantiate a current loop
    print('Instantiate a current loop.')
    cl = CurrentLoop(0, R, I, mu0)

    # Compute its magnetic field
    print('Compute a magnetic field. It may take a moment...')
    Bx, By, Bz = cl.compute_B(Xs, Ys, Zs, N=100)

    # Compute unit vectors and magnitudes of the field
    uBx, uBy, uBz, magB = unitvec(Bx, By, Bz)

    ##################
    # Do the plots
    ##################

    # Scale coordinate to plot frame
    # * Logical x in [min(Xs), max(Xs)]
    # * Plot x in [0, len(Xs)-1] (resulting from imshow)

    xl = 0
    xp = (xl - np.min(Xs))/(np.max(Xs) - np.min(Xs)) * (len(Xs)-1) + 0
    yl = 0 
    yp = (yl - np.min(Ys))/(np.max(Ys) - np.min(Ys)) * (len(Ys)-1) + 0
    zl = 0
    zp = (zl - np.min(Zs))/(np.max(Zs) - np.min(Zs)) * (len(Zs)-1) + 0

    Rl1 = -R
    Rp1 = (Rl1 - np.min(Xs))/(np.max(Xs) - np.min(Xs)) * (len(Xs)-1) + 0

    Rl2 = R
    Rp2 = (Rl2 - np.min(Xs))/(np.max(Xs) - np.min(Xs)) * (len(Xs)-1) + 0

    # Run the plots
    print('Run the plots.')
    fig, ax = plt.subplots(2, 3)
    # fig.tight_layout(rect=[0.1, 0.1, 2, 2], h_pad=4, w_pad=4) # pop-up window does not work well with this tight_layout

    # Caution: imshow reverse y-axis
    # So, pay A LOT OF ATTENTION on the y-axis.

    for n, i in enumerate([13, 14, 26]):
        plt.subplot(2,3,n+1)
        plt.imshow(magB[:,::-1,i].T, cmap = 'Reds' , interpolation = 'nearest' ) # ```::-1```: Reverse order of the y-axis, so image comes out correctly.
        plt.title('z= {:.4f}'.format(Zs[i]))
        plt.xlabel('x')
        plt.ylabel('y')
        m = 5
        ax[0,n].set_xticks(list(range(len(Xs)))[::m])             # Tick every m points
        ax[0,n].set_xticklabels(["{:.2f}".format(x) for x in Xs[::m]])

        ax[0,n].set_yticks(list(range(len(Ys)))[::m])             # Tick every m points
        ax[0,n].set_yticklabels(["{:.2f}".format(y) for y in Ys[::-1][::m]])

        plt.quiver(uBx[:,::-1,i].T, uBy[:,::-1,i].T)

        ax[0,n].set_aspect( 1 )
        loopcircle = plt.Circle(( xp , len(Ys) - 1 - yp ), (Rp2 - Rp1)/2, color='yellow', fill=False) # Y-axis starts from the top: ```len(Ys) - 1 - yp``` got it.
        ax[0,n].add_artist(loopcircle)

    print(Ys)
    for n, i in enumerate([14, 19, 21]):
        plt.subplot(2,3,n+4)
        plt.imshow(magB[:,i,::-1].T, cmap = 'Reds' , interpolation = 'nearest' )
        plt.title('y= {:.4f}'.format(Ys[i]))
        plt.xlabel('x')
        plt.ylabel('z')
        m = 5
        ax[1,n].set_xticks(list(range(len(Xs)))[::m])             # Tick every m points
        ax[1,n].set_xticklabels(["{:.2f}".format(x) for x in Xs[::m]])

        ax[1,n].set_yticks(list(range(len(Zs)))[::m])             # Tick every m points
        ax[1,n].set_yticklabels(["{:.2f}".format(z) for z in Zs[::-1][::m]])

        plt.quiver(uBx[:,i, ::-1].T, uBz[:,i, ::-1].T)


        plt.plot([Rp1, Rp2], len(Zs) - 1 - np.array([zp, zp]), 'y*-')

    plt.show()

# end def cl_viz

    
if __name__ == '__main__':

    # Define the system
    R = 0.02
    I = 3
    mu0 = 4e-7 * pi
    cl = CurrentLoop(0, R, I, mu0)

    # Points of interest
    Xs = np.arange(-0.04, 0.04, 0.003)
    Ys = np.arange(-0.04, 0.04, 0.003)
    Zs = np.arange(-0.04, 0.04, 0.003)

    # Run visualization
    cl_viz(Xs, Ys, Zs, mu0, R, I)