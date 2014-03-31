import matplotlib.pyplot as plt
from matplotlib import rc
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

from mpl_toolkits.mplot3d import Axes3D



# import things to draw arrows in 3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs
        
    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)
        
# useage example
# ax = plt.axes()
# a = Arrow3D([0,1],[0,1],[0,1], mutation_scale=20, lw=1, arrowstyle="-|>", color="k"
# ax.add_artist(a)
#
# provide: x,y,z coordinates as pairs (x0,x1),(y0,y1),(z0,z1)
# mutation_scale ->
#        


def scatter3D(x, c=None, center=None,
              cmap='spectral', cscale='log', psize=50):
    """

    if center is specified, rescales x y and z so center coordinate is 0,0,0
    """
    
    fig = plt.figure()
    ax  = fig.add_subplot(111, projection='3d')
    
    if cscale == 'log':
        c = np.log10(c)
        cmin, cmax = np.min(c), np.max(c)
        
    if np.size(center)>0:
        x = x[0] - center[0]
        y = x[1] - center[1]
        z = x[2] - center[2]
    
    # zip and sort the indexes
    zipped = zip(x,y,z,cnorm)
    
    # add each point to the plot!
    for xo, yo, zo, co in zipped:
        mappable = ax.scatter( xo, yo, zo, c=co, s=psize, cmap=cmap,
                                           vmin=cmin, vmax=cmax)
    
    
    
    
    
    return fig, ax
    
       
def drawArrow(x,  ax, v=None, t = 1.0, color="black"):
    """
    Draws arrows originating at xi,yi,zi and ending at xf,yf,zf.
    If velocity is True, xf, yf, zf is taken as velocities,
    and the arrows will be drawn along the velocity vector 
    to an end point specified by t*v_mag.
    
    x and v must be arrays of size 3 - x,y,z components
    x is the position to start the arrow... v is used to calculate
    the end point
    
    if no v is provided, x must be 6 components (x0,y0,z0,x1,y1,z1)
    
    ax is the axis object
    
    t is in the units of the plot
    """
    
    # starting position
    xs, ys, zs = x[0], x[1], x[2]
    
    
    if np.size(x) == 6:
        xf, yf, zf = x[3], x[4], x[5]
    elif not np.size(v) == 3:
        print "ERROR... VELOCITY MUST BE PROVIDED WITH v OPTION"
        print "OR A SIZE 6 ARRAY MUST BE PROVIDED FOR x:"
        print "x0,y0,z0,x1,y1,z1"

    else:
        # calculate the end position with the velocity
        final_pos = x + v*t
        
        xf, yf, zf = final_pos[0], final_pos[1], final_pos[2]

    # make the arrow using the Arrow3D class
    a = Arrow3D([xs,xf], [ys,yf], [zs,zf], mutation_scale=20, lw=1,
                arrowstyle="-|>", color=color)

    # draw the arrow                
    ax.add_artist(a)
    
    
    

        
         
