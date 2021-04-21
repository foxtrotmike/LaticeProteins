# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 00:53:08 2020

@author: fayya
"""

import numpy as np
import matplotlib.pyplot as plt
def parseAnglesNP(s2):
    s2 = np.mod(s2,360)
    dx = 1.0*(s2>=0)*(s2<45)+1.0*(s2>=315)*(s2<360)-1.0*(s2>=135)*(s2<225)
    dy = 1.0*(s2>=45)*(s2<135)-1.0*(s2>=225)*(s2<315)
    x = np.cumsum(dx)
    y = np.cumsum(dy)
    S3 = np.array([[0,0]])
    S3 = np.vstack((S3,np.vstack((x,y)).T))
    return S3
def parseAngles(s):
    """
    Plots a  path given a NEWS path string s and (optional) amino acid (H/P) string aa
    """
    s = np.mod(s,360)
    x0 = y0 = 0
    x1 = y1 = 0
    S = [(x0,y0)]
    U = set()
    for c in s:
        U.update([(x0,y0)])
        if 0<=c<45:
            y1 = y0
            x1 = x0+1
        elif 45<=c<135:
            y1 = y0+1
            x1 = x0
        elif 135<=c<225:
            y1 = y0
            x1 = x0-1
        elif 225<=c<315:
            y1 = y0-1
            x1 = x0
        elif 315<=c<360:
            y1 = y0
            x1 = x0+1
        #assert (x1,y1) not in U #self-avoiding check        
        S.append((x1,y1))
        #print x0,y0,x1,y1
        x0=x1
        y0=y1
    
    return S
def parseNEWS(s):
    """
    Plots a  path given a NEWS path string s and (optional) amino acid (H/P) string aa
    """
    x0 = y0 = 0
    x1 = y1 = 0
    S = [(x0,y0)]
    U = set()
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

        
        #assert (x1,y1) not in U #self-avoiding check
        
        S.append((x1,y1))
        #print x0,y0,x1,y1
        x0=x1
        y0=y1
    
    return S

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
    def plotAA():
        if aa[i]=='H':
            plt.plot(x1,y1,'bo')
        elif aa[i]=='P':
            plt.plot(x1,y1,'rs')
        else:
            plt.plot(x1,y1,'k.')
    plotAA()
    S = [(x0,y0)]
    U = set()
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
        #assert (x1,y1) not in U #self-avoiding check
        ax.arrow(x0, y0, x1-x0, y1-y0,head_width=0.05, head_length=0.05, fc='k', ec='k')
        plotAA()
        S.append((x1,y1))
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
    return S
def plotPath(S,aa=None):
    if aa is None:
        aa = '0'*(len(S))
    plt.figure()
    ax = plt.axes()
    i = 0
    x0 = y0 = S[0][0]
    x1 = y1 = S[0][1]
    def plotAA():
        if aa[i]=='H':
            plt.plot(x1,y1,'bo')
        elif aa[i]=='P':
            plt.plot(x1,y1,'rs')
        else:
            plt.plot(x1,y1,'k.')
    plotAA()    
    for i in range(1,len(S)):
        x1,y1=S[i]        
        ax.arrow(x0, y0, x1-x0, y1-y0,head_width=0.02, head_length=0.02, fc='k', ec='k')
        plotAA()        
        x0=x1
        y0=y1
    xmin = ymin = -len(S)
    xmax = ymax = len(S)
    plt.axis([xmin,xmax,ymin,ymax])
    minor_ticks = range(xmin,xmax)
    ax.set_xticks(minor_ticks, minor=True)                                           
    ax.set_yticks(minor_ticks, minor=True)  
    ax.grid(which='both')                                                            
    plt.show()
        
if __name__=='__main__':
    import random
    s ='NNNNNESSSSSSWWNNN'# ''.join([random.choice('NEWS') for _ in range(40)])#
    aa = ''.join([random.choice('HP') for _ in range(len(s)+1)]) #ppphhpphhppppphhhhhhhpphhpppphhpphpp
    S = parseNEWS(s)
    plotPath(S,aa)
    news2a = {'N':90,'E':0,'W':180,'S':270}
    s2 = np.array([news2a[a] for a in s])
    S2 = parseAnglesNP(s2)
    plotPath(S2,aa)
    1/0
    S = showPath(s,aa)
    Emap={'HH':-3,'PP':0,'HP':0,'PH':0}
    
    D = dict(zip(S,zip(list(range(len(aa))),aa)))
    E = 0.0
    for (x,y) in D:
        n,c = D[(x,y)]
        P = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        for p in P:
            if p in D:
                n1,c1 = D[p]
                if abs(n-n1)>1:
                    E+=Emap[c+c1]
    print(E)
        
