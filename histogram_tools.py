import numpy as np


def digitize2d(xvals, yvals, xbins, ybins):
    """
    wrapper on np.ditize to loop over a 2d histogram.
    
    

    """

    xindex = np.digitize(xvals, xbins)
    yindex = np.digitize(yvals, ybins)
