import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def my_histogram2d(x, y, xbins=None, ybins=None, logscale=False,
                                                  vfloor = None):

    """
    x and y are the horizontal and vertical axes to histogram

    xbins and ybins are optional bins... otherwise will let
    np.histogram2d decide them for you

    vfloor sets the floor of the histogram (i.e. what do
    empty bins equal). None defaults to 1 for logscale = True
    and 0 for logscale = False.

    logscale = returns np.log10(H)

    ----
    returns xmesh, ymesh, and H that can be directly
    supplied to pcolormesh for plotting

    """


    if xbins == None or ybins == None:
        H, xbins, ybins = np.histogram2d(x,y)
    else:
        H, xbins, ybins = np.histogram2d(x,y, bins=(xbins,ybins))


    ybinsize = ybins[1]-ybins[0]
    xbinsize = xbins[1] - xbins[0]

    

    ymesh, xmesh = np.meshgrid(ybins - 0.5*ybinsize, xbins - 0.5*xbinsize)
    

    if vfloor == None and logscale == True:
        H[H==0] = 1
        H = np.log10(H)
    elif not vfloor == None:
        H[H==0] = vfloor
    


    return xmesh, ymesh, H
    

def draw_circle(ax, r, center = np.zeros(3), 
                phi = np.pi, rotation_angle = 0.0,
                npoints = 40, filled = False, **kwargs):
    """
    Draws a circle on the passed axes object (ax) with a
    radius r at the center provided (default is origin).
    Filled option currenlty does nothing

    If ax is Axes3D, draws a wireframe cirlce at the angle phi
    (default pi), rotated by rotation_angle (default 0) 
    about the z axis. With defaults, circle is drawn on wireframe
    at origin in the xy plane:

    For Axes3d, drawing circles in planes:
    xy plane : phi = pi (default), rotation_angle =  0 (default)
    yz plane : phi =  0          , rotation angle =  0 (default) 
    xy plane : phi =  0 (default), rotation_angle = pi
    """

    # wireframe if 3D axes
    if isinstance(ax, Axes3D):
        if (npoints % 2) == 1:
            npoints += 1

        u, v = np.linspace(0,2*np.pi,npoints  ),\
               np.linspace(phi, phi, npoints/2) 
 
        v, u = np.meshgrid(u,v)
        u, v = u.transpose(), v.transpose()

        x    = r * np.cos(u) * np.sin(v)
        y    = r * np.sin(u) * np.sin(v)
        z    =             r * np.cos(v)

        x = x - center[0]; y = y - center[1]; z = z - center[2]

        # do the rotation
        x =   x * np.cos(rotation_angle) +\
              y * np.sin(rotation_angle)

        y = - x * np.cos(rotation_angle) +\
              y * np.cos(rotation_angle)
        # z does not change

        circle = ax.plot_wireframe(x, y, z, kwargs)
    else:
        theta = np.linspace(0.0, 2.0*np.pi, npoints)
        x, y = r * np.cos(theta), r * np.sin(theta)
   
        x = x - center[0]
        y = y - center[0]

        cirlce = ax.plot(x, y, kwargs)

    return circle 

def draw_sphere(ax, r, center = np.zeros(3), npoints = 40, **kwargs):
    """
    given a 3d figure and axis, draws a sphere and returns 
    the reference. Does not check to make sure it is a 
    3D object. kwargs passed to Axes3D.plot_wireframe
    """

    if (npoints % 2) == 1:
        npoints += 1

    u, v = np.linspace(0,2*np.pi,npoints  ),\
           np.linspace(0,  np.pi,npoints/2)
    v, u = np.meshgrid(u,v)
    u, v = u.transpose(), v.transpose()

    x    = r * np.cos(u) * np.sin(v)
    y    = r * np.sin(u) * np.sin(v)
    z    =             r * np.cos(v)

    x = x - center[0]
    y = y - center[1]
    z = z - center[2] 

    sphere = ax.plot_wireframe(x, y, z, kwargs)

    return sphere
