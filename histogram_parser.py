# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:49:47 2015

@author: pedro.correia
"""

from __future__ import division            # Just making sure that correct integer division is working
import numpy as np                         # This is numpy,python numerical library
import matplotlib.pyplot as plt            # This is the very well known plot library matplotlib
import objects_parser as obj               # Our local objects library.

import scipy.stats as st        # Important to do linear regression

def plot_single_histogram(data,sheet,variable,title,opath,bins=30,color='red',alpha=1.0,normed=True,checkopen=False,dpi=90):
    """
    important args: data,sheet,variable,title,opath
    This function will launch (if requested) and save a simple histogram to file.
    The arguments are: data (for excel object), bins (integer), color (name or hex),
    normed (boolean), checkopen (boolean), dip.
    """
    fontdict = {'fontsize': 12,'fontweight' : 'bold','verticalalignment': 'baseline','horizontalalignment': 'center'}
    ind = np.where(data.me[sheet][variable]!=data.null)
    fig = plt.figure(num = None, dpi=dpi)
    ax = fig.add_subplot(111, frame_on=True)
    ax.hist(data.me[sheet][variable][ind],bins=bins,color=color,alpha=alpha,normed=normed)
    ax.grid(which='both',axis='both')
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(10) 
        tick.label.set_rotation(45)
    ax.set_title(title,fontdict)
    plt.savefig(opath)
    if checkopen:
        plt.show()
    plt.close()
    
def plot_double_histogram(data1,data2,sheet1,sheet2,variable1,variable2,title,opath,bins=30,color1='red',color2='green',labels=['1','2'],alpha=1.0,normed=True,checkopen=False,dpi=90):
    """
    important args: data1,data2,sheet1,sheet2,variable1,variable2,title,opath
    This function will launch (if requested) and save a double histogram to file.
    The arguments are: data (for excel object), bins (integer), color (name or hex),
    normed (boolean), checkopen (boolean), dip. This was made to compare two variables.
    """
    fontdict = {'fontsize': 12,'fontweight' : 'bold','verticalalignment': 'baseline','horizontalalignment': 'center'}
    ind1 = np.where(data1.me[sheet1][variable1]!=data1.null)
    ind2 = np.where(data2.me[sheet2][variable2]!=data2.null)
    hmin = (data1.me[sheet1][variable1][ind1].min(),data2.me[sheet2][variable2][ind2].min())
    hmax = (data1.me[sheet1][variable1][ind1].max(),data2.me[sheet2][variable2][ind2].max())
    fig = plt.figure(num = None, dpi=dpi)
    ax = fig.add_subplot(111, frame_on=True)
    ax.hist((data1.me[sheet1][variable1][ind1],data2.me[sheet2][variable2][ind2]),bins=bins,color=[color1,color2],range=(min(hmin),max(hmax)),alpha=alpha,normed=normed,label=labels)
    ax.grid(which='both',axis='both')
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(10) 
        tick.label.set_rotation(45)
    ax.set_title(title,fontdict)
    ax.legend(loc='best')
    plt.savefig(opath)
    if checkopen:
        plt.show()
    plt.close()
    
def plot_triple_histogram(data1,data2,data3,sheet1,sheet2,sheet3,variable1,variable2,variable3,title,opath,bins=30,color1='blue',color2='red',color3='green',labels=['1','2','3'],alpha=1.0,normed=True,checkopen=False,dpi=90):
    """
    important args: data1,data2,sheet1,sheet2,variable1,variable2,title,opath
    This function will launch (if requested) and save a double histogram to file.
    The arguments are: data (for excel object), bins (integer), color (name or hex),
    normed (boolean), checkopen (boolean), dip. This was made to compare two variables.
    """
    fontdict = {'fontsize': 12,'fontweight' : 'bold','verticalalignment': 'baseline','horizontalalignment': 'center'}
    ind1 = np.where(data1.me[sheet1][variable1]!=data1.null)
    ind2 = np.where(data2.me[sheet2][variable2]!=data2.null)
    ind3 = np.where(data3.me[sheet3][variable3]!=data3.null)
    hmin = (data1.me[sheet1][variable1][ind1].min(),data2.me[sheet2][variable2][ind2].min(),data3.me[sheet3][variable3][ind3].min())
    hmax = (data1.me[sheet1][variable1][ind1].max(),data2.me[sheet2][variable2][ind2].max(),data3.me[sheet3][variable3][ind3].max())
    fig = plt.figure(num = None, dpi=dpi)
    ax = fig.add_subplot(111, frame_on=True)
    ax.hist((data1.me[sheet1][variable1][ind1],data2.me[sheet2][variable2][ind2],data3.me[sheet3][variable3][ind3]),bins=bins,color=[color1,color2,color3],range=(min(hmin),max(hmax)),alpha=alpha,normed=normed,label=labels)
    ax.grid(which='both',axis='both')
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(10) 
        tick.label.set_rotation(45)
    ax.set_title(title,fontdict)
    ax.legend(loc='best')
    plt.savefig(opath)
    if checkopen:
        plt.show()
    plt.close()
    
def plot_scatterplot(data,sheet,variable1,variable2,title,opath,color='red',size=120,alpha=1.0,linreg=True,checkopen=False,dpi=90):
    """
    important args: data,sheet,variable1,variable2,title,opath
    This functions will launch (checkopen=True) and save a double histogram to file
    opath.
    """
    fontdict = {'fontsize': 12,'fontweight' : 'bold','verticalalignment': 'baseline','horizontalalignment': 'center'}
    ind = np.where((data.me[sheet][variable1]!=data.null) & (data.me[sheet][variable2]!=data.null))   
    fig = plt.figure(num = None, dpi=dpi)
    ax = fig.add_subplot(111, frame_on=True)
    ax.scatter(data.me[sheet][variable1][ind],data.me[sheet][variable2][ind],color=color,s=size,alpha=alpha)
    if linreg:
        xl = np.linspace(data.me[sheet][variable1][ind].min(),data.me[sheet][variable1][ind].max(),100)
        m,b,r,p,std = st.linregress(data.me[sheet][variable1][ind],data.me[sheet][variable2][ind])        
        yl = m*xl+b
        ax.plot(xl,yl,color=color,linestyle='--')
    ax.grid(which='both',axis='both')
    for tick in ax.xaxis.get_major_ticks():
        tick.label.set_fontsize(10) 
        tick.label.set_rotation(45)
    ax.set_title(title,fontdict)
    plt.savefig(opath)
    if checkopen:
        plt.show()
    plt.close()
    
def plot_single_variogram(tup,sill,title,opath):
    """
    This function will save to file a single variable variogram.
    """
    fig = plt.figure(figsize=(8,8),dpi=120)
    plt.scatter(tup[1],tup[0],color='green',s=220)
    plt.title(title)
    plt.plot([0,tup[1].max()],[sill,sill],color='red',linewidth=3)
    plt.grid()
    plt.xlabel('Distancia (h)')
    plt.ylabel('semi-variograma')
    plt.xlim(0,tup[1].max())
    plt.ylim(0,sill+0.05*sill)
    plt.savefig(opath+'.png')
    plt.close()
    
def plot_double_variogram(tup,tup2,sill,sill2,title,opath):
    """
    This function will save to file to variogram plot variables.
    """
    fig = plt.figure(figsize=(8,8),dpi=120)
    plt.scatter(tup[1],tup[0]/sill,color='green',s=220)
    plt.scatter(tup2[1],tup2[0]/sill2,color='blue',s=220)
    plt.title(title)
    plt.plot([0,tup[1].max()],[1,1],color='red',linewidth=3)
    plt.grid()
    plt.xlabel('Distancia (h)')
    plt.ylabel('semi-variograma')
    plt.xlim(0,tup[1].max())
    plt.ylim(0,1+0.05*1)
    plt.savefig(opath+'.png')
    plt.close()
    
def plot_ppplot(obj1,sheet1,variable1,obj2,sheet2,variable2,title,opath):
    """
    This function will create a pp-plot and save to a file.
    """
    p1 = np.percentile(obj1.me[sheet1][variable1],range(0,101,1))
    p2 = np.percentile(obj2.me[sheet2][variable2],range(0,101,1))
    p1c = np.cumsum(np.array(p1))/np.cumsum(np.array(p1)).max()
    p2c = np.cumsum(np.array(p2))/np.cumsum(np.array(p2)).max()
    fig = plt.figure(figsize=(8,8),dpi=120)
    plt.scatter(p1c,p2c,color='#566c73',s=30)
    plt.plot([0,1],[0,1],color='red',alpha=0.3)
    plt.xlim(0,1)
    plt.ylim(0,1)
    plt.grid()
    plt.xlabel(sheet1+'_'+variable1)
    plt.ylabel(sheet2+'_'+variable2)
    plt.title(title)
    plt.savefig(opath+'.png')
    plt.close()
