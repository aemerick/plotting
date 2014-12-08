import matplotlib.pyplot as plt
from   matplotlib import rc
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

def scatterpie(x,y,c,psize=50.0,cmap='spectral',cbarLabel='', clim = None, default_marker = "o", fig=None, ax = None):
    """
    makes a scatter plot with pies as the points
    
    x:
    x coordinate of point
    
    y:
    y coordinate of point
    
    c:
    color for those coordinates. Pie chart used for a point if there
    are two c's for a given x and y
    """
    # load the linear segmented color map object
    cmapObj = plt.cm.get_cmap(cmap)
    
    # set up plot
    newfig=False
    if fig == None:
        fig = plt.figure(figsize=[6,6])
        newfig=True
    if ax == None:
        ax  = fig.add_subplot(111)

    
    #find the full range of the color map to use:
    #convert c to normalized units
    if clim == None:
        cmin, cmax = np.min(c), np.max(c)
    else:
        cmin, cmax = clim[0], clim[1]
    

    cnorm = c
    
    # zip and sort the indexes
    zipped = zip(x,y,cnorm)
    dtype  = [('x',float),('y',float),('c',float)]
    
    zipped = np.array(zipped,dtype = dtype)
    # sort by x then by y
    zs     = np.sort(zipped,order=['x','y'])  
    
    # loop through
    i = 0

 
    while i < np.size(zs):
        
        xyc = zs[i]
        xyc_list = xyc
        
        j = 0
        while i + j +1 < np.size(zs):
            xyc_next = zs[i + j + 1]
           
            # if line is the same, add it to the list
            if xyc_next[0] == xyc[0] and xyc_next[1] == xyc[1]:
                xyc_list = np.append(xyc_list,xyc_next)
                j = j + 1
            else:
                break
        
        
        # now, we have a list of all points with the same stuffs
        num_points = np.size(xyc_list) # number of points with same x,y

        xyc_list = np.append(xyc_list,xyc)
        
        
        
        # set up the sizes of each pie point
        frac = 1.0 / (1.0*num_points)
        
        # make the marker sizes
        all_markers = []
        
        # if more than 1 point, use pie chart
        if num_points > 1:
            for k in np.arange(num_points):
                ll = k*frac * 2.0*np.pi
                uu = 2.0*np.pi*frac
        
                xmarker = [0] + np.cos(np.linspace(ll,ll+uu,50)).tolist()
                ymarker = [0] + np.sin(np.linspace(ll,ll+uu,50)).tolist()
                xymarker = list(zip(xmarker,ymarker))
            
                all_markers.append(xymarker)
            
            # add the points!
            for k in np.arange(num_points):
                mappable = ax.scatter(xyc_list[k][0],xyc_list[k][1], c=xyc_list[k][2],
                           marker=(all_markers[k],1), s = psize,cmap=cmap,
                           vmin=cmin,vmax=cmax)
      
        else: # else use normal scatter plot
        
            mappable = ax.scatter(xyc_list[0][0], xyc_list[0][1], c = xyc_list[0][2], marker=default_marker,
                                  s = 3.0*psize, cmap = cmap, vmin = cmin, vmax = cmax)        
        
      
        i = i + j + 1

        
    # make the plot square if x and y are square

    if newfig:
        upper = np.max([np.max(x),np.max(y)])
        lower = np.min([np.min(x),np.min(y)])
        upper = upper + 0.1*(upper-lower)
        lower = lower - 0.1*(upper-lower)
        ax.set_xlim(lower,upper)
        ax.set_ylim(lower,upper)
        x0,x1 = ax.get_xlim()
        y0,y1 = ax.get_ylim()

   # mappable = ax.scatter(0.0,0.0,c[0],vmin=cmin,vmax=cmax,cmap=cmap)
   # cbar = fig.colorbar(mappable,pad=0.15)
    
        ax.set_aspect((x1-x0)/(y1-y0))
        divider = make_axes_locatable(ax)
        cax     = divider.append_axes("right",size="2.5%",pad=0.001)
        cbar = fig.colorbar(mappable,label=cbarLabel,cax=cax)
        
    
    
    return fig, ax, mappable
    
    
    
    
    
