# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 16:11:25 2017

@author: afsar
"""
import matplotlib.pyplot as plt
def showPath(s,aa=None):
    """
    Plots a  path given a NEWS path string s and (optional) amino acid (H/P) string aa
    """
    if aa is None:
        aa = '0'*(len(s)+1)
    plt.figure()
    ax = plt.axes()
    x0 = y0 = 0
    x1 = y1 = 0
    assert len(aa)==len(s)+1
    i = 0
    U = set()
    
    def plotAA():
        if aa[i]=='H':
            plt.plot(x1,y1,'bo')
        elif aa[i]=='P':
            plt.plot(x1,y1,'rs')
        else:
            plt.plot(x1,y1,'k.')
    plotAA()
    for c in s:
        U.update([(x0,y0)])
        if c=='N':
            y1 = y0+1
            x1 = x0
        elif c=='S':
            y1 = y0-1
            x1 = x0
        elif c=='E':
            y1 = y0
            x1 = x0+1
        elif c=='W':
            y1 = y0
            x1 = x0-1

        i+=1
        assert (x1,y1) not in U #self-avoiding check
        ax.arrow(x0, y0, x1-x0, y1-y0,head_width=0.05, head_length=0.05, fc='k', ec='k')
        plotAA()
        
        #print x0,y0,x1,y1
        x0=x1
        y0=y1
        
    xmin = ymin = -len(s)
    xmax = ymax = len(s)
    plt.axis([xmin,xmax,ymin,ymax])
    minor_ticks = range(xmin,xmax)
    ax.set_xticks(minor_ticks, minor=True)                                           
    ax.set_yticks(minor_ticks, minor=True)  
    ax.grid(which='both')                                                            
    plt.show()
    return U
if __name__=='__main__':
    import random
    s = 'NNNNNEEEEESSSSSSSSWWWWWW'#''.join([random.choice('NEWS') for _ in range(4)])
    aa = ''.join([random.choice('HP') for _ in range(len(s)+1)]) #ppphhpphhppppphhhhhhhpphhpppphhpphpp
    U = showPath(s,aa)