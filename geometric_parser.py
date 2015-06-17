# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:53:19 2015

@author: pedro.correia
"""

from __future__ import division            # Just making sure that correct integer division is working
import numpy as np                         # This is numpy,python numerical library
import objects_parser as obj               # Our local objects library.

def create_object_by_interdistance(obj1,obj2,sheet1,sheet2,coords1,coords2,maxdist=3,extra=''):
    """
    This functions will receive two excel class objects and given the coord keys
    (x,y,z,variable) will create a whole new object only with the indexes of points
    in obj1 that are in a distance less than maxdist from points in obj2.
    """
    # Creating shortcut names for x,y,z in object 1
    x1 = obj1.me[sheet1][coords1[0]]
    y1 = obj1.me[sheet1][coords1[1]]
    z1 = obj1.me[sheet1][coords1[2]]
    # Creating shortcut names for x,y,z in object 2
    x2 = obj2.me[sheet2][coords2[0]]
    y2 = obj2.me[sheet2][coords2[1]]
    z2 = obj2.me[sheet2][coords2[2]]
    mask = (x2!=obj2.null)    
    
    counter = 0
    for i in xrange(x1.shape[0]):
        if x1[i]!=obj1.null and y1[i]!=obj1.null and z1[i]!=obj1.null:
            dist = np.sqrt((x1[i]-x2[mask])**2+(y1[i]-y2[mask])**2+(z1[i]-z2[mask])**2)
            if dist.min()<=maxdist:
                counter = counter + 1
    
    nx = np.zeros(counter,dtype='float32')
    ny = np.zeros(counter,dtype='float32')
    nz = np.zeros(counter,dtype='float32')
    variables = {}
    if len(coords1)>4:
        for i in xrange(3,len(coords1)):
            variables[coords1[i]] = np.zeros(counter,dtype='float32')
    else:
        variables[coords1[3]] = np.zeros(counter,dtype='float32')
    if len(extra)>0:
        variables[extra] = np.zeros(counter,dtype='|S15')
        s_extra = True
    counter = 0
    for i in xrange(x1.shape[0]):
        if x1[i]!=obj1.null and y1[i]!=obj1.null and z1[i]!=obj1.null:
            dist = np.sqrt((x1[i]-x2[mask])**2+(y1[i]-y2[mask])**2+(z1[i]-z2[mask])**2)
            if dist.min()<=maxdist:
                nx[counter] = x1[i]
                ny[counter] = y1[i]
                nz[counter] = z1[i]
                for j in xrange(3,len(coords1)):
                    variables[coords1[j]][counter] = obj1.me[sheet1][coords1[j]][i]
                if s_extra: variables[extra][counter] = obj1.me[sheet1][extra][i]
                counter = counter + 1
    variables[coords1[0]] = nx
    variables[coords1[1]] = ny
    variables[coords1[2]] = nz
    result = {}
    result[sheet1] = variables
    return obj.excelObject(result,obj1.null)
    
def create_scatter_object_by_interdistance(obj1,obj2,sheet1,sheet2,coords1,coords2,extra='2',maxdist=3):
    """
    FROM: create_object_by_interdistance
    This functions will receive two excel class objects and given the coord keys
    (x,y,z,variable) will create a whole new object only with the indexes of points
    in obj1 that are in a distance less than maxdist from points in obj2.
    FROM: create_scatter_object_by_interdistance
    The difference from the first is that the return object has one extra variable
    which is the closest point from obj2.
    """
    # Creating shortcut names for x,y,z in object 1
    x1 = obj1.me[sheet1][coords1[0]]
    y1 = obj1.me[sheet1][coords1[1]]
    z1 = obj1.me[sheet1][coords1[2]]
    # Creating shortcut names for x,y,z in object 2
    x2 = obj2.me[sheet2][coords2[0]]
    y2 = obj2.me[sheet2][coords2[1]]
    z2 = obj2.me[sheet2][coords2[2]]
    mask = (x2!=obj2.null)    
    
    counter = 0
    for i in xrange(x1.shape[0]):
        if x1[i]!=obj1.null and y1[i]!=obj1.null and z1[i]!=obj1.null:
            dist = np.sqrt((x1[i]-x2[mask])**2+(y1[i]-y2[mask])**2+(z1[i]-z2[mask])**2)
            if dist.min()<=maxdist:
                counter = counter + 1

    nx = np.zeros(counter,dtype='float32')
    ny = np.zeros(counter,dtype='float32')
    nz = np.zeros(counter,dtype='float32')
    variables = {}
    if len(coords1)>4:
        for i in xrange(3,len(coords1)):
            variables[coords1[i]] = np.zeros(counter,dtype='float32')
    else:
        variables[coords1[3]] = np.zeros(counter,dtype='float32')
    variables[coords2[3]+extra] = np.zeros(counter,dtype='float32')
    
    counter = 0
    for i in xrange(x1.shape[0]):
        if x1[i]!=obj1.null and y1[i]!=obj1.null and z1[i]!=obj1.null:
            dist = np.sqrt((x1[i]-x2[mask])**2+(y1[i]-y2[mask])**2+(z1[i]-z2[mask])**2)
            if dist.min()<=maxdist:
                nx[counter] = x1[i]
                ny[counter] = y1[i]
                nz[counter] = z1[i]
                for j in xrange(3,len(coords1)):
                    variables[coords1[j]][counter] = obj1.me[sheet1][coords1[j]][i]
                indx = dist.argmin()
                variables[coords2[3]+extra][counter] = obj2.me[sheet2][coords2[2]][mask][indx]
                counter = counter + 1
    variables[coords1[0]] = nx
    variables[coords1[1]] = ny
    variables[coords1[2]] = nz
    result = {}
    result[sheet1] = variables
    return obj.excelObject(result,obj1.null)
    
def create_object_by_type(obj1,sheet,variables,variable,value):
    """
    This function will build a new object from an old one considering only
    the values = value from variable variable. The chosen variables for the
    new object are the variables list.
    """
    ind = np.where(obj1.me[sheet][variable]==value)
    result = {}
    local = {}
    for i in variables:
        local[i] = obj1.me[sheet][i][ind]
    result[sheet] = local
    return obj.excelObject(result,obj1.null)
    
def calculate_variogram(obj1,sheet,variables):
    """
    This function will create a variogram table that can latter be used to
    compute a directional variogram (there's a directional_variogram function).
    """
    x = obj1.me[sheet][variables[0]]
    y = obj1.me[sheet][variables[1]]
    z = obj1.me[sheet][variables[2]]
    v = obj1.me[sheet][variables[3]]
    full_size = np.sum(xrange(x.shape[0]))-x.shape[0]+1
    variogram_list = np.zeros((full_size,5),dtype='float32')
    variogram_list[:,:] = -99
    counter = 0
    l = x.shape[0]
    for i in xrange(1,l-1):
        distx = (x[i+1:]-x[i])
        disty = (y[i+1:]-y[i])
        distz = (z[i+1:]-z[i])
        azimuth = np.arctan2(np.abs(distx),np.abs(disty))*180/np.pi
        Q2 = np.where((distx<0) & (disty>0))
        Q4 = np.where((distx>0) & (disty<0))
        azimuth[Q2[0]] = azimuth[Q2[0]]*-1
        azimuth[Q4[0]] = azimuth[Q4[0]]*-1
        dip = np.arctan2(distz,np.sqrt(distx**2+disty**2))*180/np.pi #np.arctan2(distz,np.sqrt(distx**2+disty**2))*180/np.pi
        dist = np.sqrt(distx**2+disty**2+distz**2)
        var = (v[i+1:]-v[i])**2
        variogram_list[counter:counter+(l-i-1),0] = dist[:]
        variogram_list[counter:counter+(l-i-1),1] = azimuth[:]
        variogram_list[counter:counter+(l-i-1),2] = dip[:]
        variogram_list[counter:counter+(l-i-1),3] = var[:]
        variogram_list[counter:counter+(l-i-1),4] = np.abs(distz[:])
        counter = counter+(l-i-1)
    return variogram_list
        
def directional_variogram(variogram_list,azimuth,dip,tolerance,bins,maximum=False,dz=False):
    """
    This function will return a the arrays necessary to plot an experimental
    variogram. You'll need first to calculate the variogram table using
    calculate_variogram function.
    """
    if type(maximum)==bool: maximum = variogram_list[:,0].max()
    if dip==0:
        if type(dz)==bool:
            ind0 = np.where((variogram_list[:,1]<=azimuth+tolerance) & (variogram_list[:,1] >= azimuth - tolerance) & (variogram_list[:,2]<=dip+tolerance) & (variogram_list[:,2] >= dip - tolerance))
            if azimuth+tolerance>90:
                dif = -90 + (azimuth + tolerance - 90)
                ind0b = np.where((variogram_list[:,1]<=dif) & (variogram_list[:,2]<=dip+tolerance) & (variogram_list[:,2] >= dip - tolerance))
                ind0 = (np.hstack((ind0[0],ind0b[0])),)
            elif azimuth-tolerance<-90:
                dif = 90 - np.abs((azimuth - tolerance + 90))
                ind0b = np.where((variogram_list[:,1]>=dif) & (variogram_list[:,2]<=dip+tolerance) & (variogram_list[:,2] >= dip - tolerance))
                ind0 = (np.hstack((ind0[0],ind0b[0])),)
        else:
            ind0 = np.where((variogram_list[:,1]<=azimuth+tolerance) & (variogram_list[:,1] >= azimuth - tolerance) & (variogram_list[:,2]<=dip+tolerance) & (variogram_list[:,2] >= dip - tolerance) & (variogram_list[:,4]<=dz))
            if azimuth+tolerance>90:
                dif = -90 + (azimuth + tolerance - 90)
                ind0b = np.where((variogram_list[:,1]<=dif) & (variogram_list[:,2]<=dip+tolerance) & (variogram_list[:,2] >= dip - tolerance) & (variogram_list[:,4]<=dz))
                ind0 = (np.hstack((ind0[0],ind0b[0])),)
            elif azimuth-tolerance<-90:
                dif = 90 - np.abs((azimuth - tolerance + 90))
                ind0b = np.where((variogram_list[:,1]>=dif) & (variogram_list[:,2]<=dip+tolerance) & (variogram_list[:,2] >= dip - tolerance) & (variogram_list[:,4]<=dz))
                ind0 = (np.hstack((ind0[0],ind0b[0])),)
    else:
        ind0 = np.where((variogram_list[:,2]<=dip+tolerance) & (variogram_list[:,2] >= dip - tolerance))
    countsPerBin = np.histogram(variogram_list[ind0,0],bins=bins,range=[0,maximum])
    sumsPerBin = np.histogram(variogram_list[ind0,0],bins=bins,range=[0,maximum], weights=variogram_list[ind0,3])
    ind = np.where(countsPerBin[0]!=0)
    average = sumsPerBin[0][ind] / countsPerBin[0][ind]
    if len(average)>0:
        return (average/2,sumsPerBin[1][ind]+(sumsPerBin[1][1]-sumsPerBin[1][0])/2)
    else:
        return (np.array([-10,-10,-10]),np.array([30,70,maximum]))
