# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 16:29:08 2015

@author: pedro.correia
"""

from __future__ import division            # Just making sure that correct integer division is working
import numpy as np                         # This is numpy,python numerical library
import objects_parser as obj               # Our local objects library.

import scipy.stats as st                   # Important to do linear regression

def produce_report_on_file(obj1,sheet1,variables1,opath):
    """
    This function will do a an ASCII report with the given data.
    """
    fid = open(opath,'w')
    fid.write('NOTE: This report is dealing with '+sheet1+' sheet on given object.\n')
    fid.write('The requested variables are:\n')
    for i in xrange(len(variables1)):
        fid.write(str(i)+') '+variables1[i]+'\n')
    fid.write('\n')
    fid.write('[STATS-TABLE] #########################################>')
    fid.write('\n%20s'%'Stats-Vrbls')
    for i in xrange(len(variables1)):
        fid.write('%20s'%variables1[i])
    fid.write('\n%20s'%'Minimum')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20.3f'%np.min(obj1.me[sheet1][variables1[i]][ind]))
    fid.write('\n%20s'%'Per25')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20.3f'%np.percentile(obj1.me[sheet1][variables1[i]][ind],25))
    fid.write('\n%20s'%'Per50')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20.3f'%np.percentile(obj1.me[sheet1][variables1[i]][ind],50))
    fid.write('\n%20s'%'Per75')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20.3f'%np.percentile(obj1.me[sheet1][variables1[i]][ind],75))
    fid.write('\n%20s'%'Maximum')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20.3f'%np.max(obj1.me[sheet1][variables1[i]][ind]))
    fid.write('\n%20s'%'Mean')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20.3f'%np.mean(obj1.me[sheet1][variables1[i]][ind]))
    fid.write('\n%20s'%'Std')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20.3f'%np.std(obj1.me[sheet1][variables1[i]][ind]))
    fid.write('\n%20s'%'Var')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20.3f'%np.var(obj1.me[sheet1][variables1[i]][ind]))
    fid.write('\n%20s'%'Number')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20i'%obj1.me[sheet1][variables1[i]][ind].shape[0])
    fid.write('\n[END] #################################################>\n\n')

    fid.write('[PEARSON-TABLE] #######################################>')
    fid.write('\n%20s'%'Vrbls-Vrbls')
    for i in xrange(len(variables1)):
        fid.write('%20s'%variables1[i])
    for i in xrange(len(variables1)):
        fid.write('\n%20s'%variables1[i])
        for j in xrange(len(variables1)):
            ind = np.where((obj1.me[sheet1][variables1[i]]!=obj1.null) & (obj1.me[sheet1][variables1[j]]!=obj1.null))
            m,b,r,p,std = st.linregress(obj1.me[sheet1][variables1[j]][ind],obj1.me[sheet1][variables1[i]][ind])        
            fid.write('%20.3f'%r)
    fid.write('\n[END] #################################################>\n\n')
    fid.close()


def produce_double_report_on_file(obj1,sheet1,variables1,obj2,sheet2,variables2,opath):
    """
    This function will do a an ASCII report with the given data.
    """
    fid = open(opath,'w')
    fid.write('NOTE: This report is dealing with '+sheet1+' and '+sheet2+' sheets on two given objects.\n')
    fid.write('The requested variables are:\n')
    for i in xrange(len(variables1)):
        fid.write(str(i)+') '+variables1[i]+'\n')
    for j in xrange(len(variables2)):
        fid.write(str(j)+') '+variables2[j]+'\n')
    fid.write('\n')
    fid.write('[STATS-TABLE] #########################################>')
    fid.write('\n%20s'%'Stats-Vrbls')
    for i in xrange(len(variables1)):
        fid.write('%20s'%('A_'+variables1[i]))
    for j in xrange(len(variables2)):
        fid.write('%20s'%('B_'+variables2[j]))
    fid.write('\n%20s'%'Minimum')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20.3f'%np.min(obj1.me[sheet1][variables1[i]][ind]))
    for j in xrange(len(variables2)):
        ind = np.where(obj2.me[sheet2][variables2[j]]!=obj2.null)
        fid.write('%20.3f'%np.min(obj2.me[sheet2][variables2[j]][ind]))
    fid.write('\n%20s'%'Per25')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20.3f'%np.percentile(obj1.me[sheet1][variables1[i]][ind],25))
    for j in xrange(len(variables2)):
        ind = np.where(obj2.me[sheet2][variables2[j]]!=obj2.null)
        fid.write('%20.3f'%np.percentile(obj2.me[sheet2][variables2[j]][ind],25))
    fid.write('\n%20s'%'Per50')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20.3f'%np.percentile(obj1.me[sheet1][variables1[i]][ind],50))
    for j in xrange(len(variables2)):
        ind = np.where(obj2.me[sheet2][variables2[j]]!=obj2.null)
        fid.write('%20.3f'%np.percentile(obj2.me[sheet2][variables2[j]][ind],50))
    fid.write('\n%20s'%'Per75')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20.3f'%np.percentile(obj1.me[sheet1][variables1[i]][ind],75))
    for j in xrange(len(variables2)):
        ind = np.where(obj2.me[sheet2][variables2[j]]!=obj2.null)
        fid.write('%20.3f'%np.percentile(obj2.me[sheet2][variables2[j]][ind],75))
    fid.write('\n%20s'%'Maximum')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20.3f'%np.max(obj1.me[sheet1][variables1[i]][ind]))
    for j in xrange(len(variables2)):
        ind = np.where(obj2.me[sheet2][variables2[j]]!=obj2.null)
        fid.write('%20.3f'%np.max(obj2.me[sheet2][variables2[j]][ind]))
    fid.write('\n%20s'%'Mean')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20.3f'%np.mean(obj1.me[sheet1][variables1[i]][ind]))
    for j in xrange(len(variables2)):
        ind = np.where(obj2.me[sheet2][variables2[j]]!=obj2.null)
        fid.write('%20.3f'%np.mean(obj2.me[sheet2][variables2[j]][ind]))
    fid.write('\n%20s'%'Std')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20.3f'%np.std(obj1.me[sheet1][variables1[i]][ind]))
    for j in xrange(len(variables2)):
        ind = np.where(obj2.me[sheet2][variables2[j]]!=obj2.null)
        fid.write('%20.3f'%np.std(obj2.me[sheet2][variables2[j]][ind]))
    fid.write('\n%20s'%'Var')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20.3f'%np.var(obj1.me[sheet1][variables1[i]][ind]))
    for j in xrange(len(variables2)):
        ind = np.where(obj2.me[sheet2][variables2[j]]!=obj2.null)
        fid.write('%20.3f'%np.var(obj2.me[sheet2][variables2[j]][ind]))
    fid.write('\n%20s'%'Number')
    for i in xrange(len(variables1)):
        ind = np.where(obj1.me[sheet1][variables1[i]]!=obj1.null)
        fid.write('%20i'%obj1.me[sheet1][variables1[i]][ind].shape[0])
    for i in xrange(len(variables2)):
        ind = np.where(obj2.me[sheet2][variables2[i]]!=obj2.null)
        fid.write('%20i'%obj2.me[sheet2][variables2[i]][ind].shape[0])
    fid.write('\n[END] #################################################>\n\n')
    
    fid.write('[PEARSON-TABLE] #######################################>')
    fid.write('\n%20s'%'Vrbls-Vrbls')
    for i in xrange(len(variables1)):
        fid.write('%20s'%('A_'+variables1[i]))
    for i in xrange(len(variables1)):
        fid.write('\n%20s'%('A_'+variables1[i]))
        for j in xrange(len(variables1)):
            ind = np.where((obj1.me[sheet1][variables1[i]]!=obj1.null) & (obj1.me[sheet1][variables1[j]]!=obj1.null))
            m,b,r,p,std = st.linregress(obj1.me[sheet1][variables1[j]][ind],obj1.me[sheet1][variables1[i]][ind])        
            fid.write('%20.3f'%r)
    fid.write('\n[END] #################################################>\n\n')

    fid.write('[PEARSON-TABLE] #######################################>')
    fid.write('\n%20s'%'Vrbls-Vrbls')
    for i in xrange(len(variables1)):
        fid.write('%20s'%('B_'+variables2[i]))
    for i in xrange(len(variables1)):
        fid.write('\n%20s'%('B_'+variables2[i]))
        for j in xrange(len(variables1)):
            ind = np.where((obj2.me[sheet2][variables2[i]]!=obj2.null) & (obj2.me[sheet2][variables2[j]]!=obj2.null))
            m,b,r,p,std = st.linregress(obj2.me[sheet2][variables2[j]][ind],obj2.me[sheet2][variables2[i]][ind])        
            fid.write('%20.3f'%r)
    fid.write('\n[END] #################################################>\n\n')        
    fid.close()

def create_distribution_file(obj1,sheet1,variable1,opath):
    """
    This function will create a specific file to be added to Simdist software
    data base.
    """
    p = np.percentile(obj1.me[sheet1][variable1],range(0,101,1))  # Getting percentile value (0 to 100)
    res = np.zeros((len(p),2),dtype='float32')                # Creating the base matrix to be put in file.
    res[:,0] = np.arange(0,101,1)[:]                              # adding percentile point
    res[:,1] = p[:]                                               # adding percentile value
    np.savetxt(opath,res,fmt='%10.3f')                            # saving result to file
    
