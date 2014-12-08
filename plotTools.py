import numpy as np
import matplotlib.pyplot as plt



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
    


