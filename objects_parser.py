# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:36:06 2015

@author: pedro.correia
"""

from __future__ import division  # Just making sure that correct integer division is working
import numpy as np               # This is numpy,python numerical library
import file_parser as fp         # This is our local file_parsing library

class dataObject():
    """
    Data object stores information in a more convetional way than excelObject.
    User gives a 2D numpy array and a list with the name of each variable.
    """
    def __init__(self,data,header):
        self.data   = data         # Storing data (notice I'm not testing it)
        self.header = header       # Storing header (which I'm not testing also)
        
    def get_variable_by_name(self,name):
        """
        This function returns the array of the variable requested by string name.
        """
        if type(name)!=type(''): self.error(name,' should be a valid variable string name.')
        if name not in self.header: self.error(name,' is not a valid variable for this object.')
        return self.data[self.header.index[name]]
        
    def get_variable_by_index(self,ind):
        """
        This function returns the array of the variable requested by integer index.
        """
        if type(ind)!=type(1): self.error(ind,' should be a valid variable integer index.')
        if ind<0 or ind> self.data.shape[1]: self.error(ind,' must be within the indexes of the data on this class.')
        return self.data[:,ind]

class pointObject():
    """
    Point object stores information in a more convetional way than excelObject.
    User gives a 2D numpy array and a list with the name of each variable. Also
    the x,y and z (if not Z than z=None) arrays.
    """
    def __init__(self,data,header,x,y,z=None):
        self.data   = data         # Storing data (notice I'm not testing it)
        self.header = header       # Storing header (which I'm not testing also)
        self.x      = x
        self.y      = y
        if z!=None:
            self.z  = z
        else:
            self.z  = np.zeros(self.x.shape,dtype='float32')
            
    def get_coordinates(self):
        """
        Function without arguments to quickly return a tuple with the three
        coordinate arrays.
        """
        return self.x,self.y,self.z
            
    def get_variable_by_name(self,name):
        """
        This function returns the array of the variable requested by string name.
        """
        if name == 'x': return self.x
        if name == 'y': return self.y
        if name == 'z': return self.z
        if type(name)!=type(''): self.error(name,' should be a valid variable string name.')
        if name not in self.header: self.error(name,' is not a valid variable for this object.')
        return self.data[self.header.index[name]]
        
    def get_variable_by_index(self,ind):
        """
        This function returns the array of the variable requested by integer index.
        """
        if type(ind)!=type(1): self.error(ind,' should be a valid variable integer index.')
        if ind<0 or ind> self.data.shape[1]: self.error(ind,' must be within the indexes of the data on this class.')
        return self.data[:,ind]

class excelObject():
    """
    Excel object stores all information from an excel file into a dictionary of
    dictionaries and deals with that information using high-level functions. The
    input is the dictionary of dictionaries. open_excel_file function returns
    this object.
    """
    def __init__(self,data,null=-999):
        self.me = data                      # This is the local variable that has the dictionaries with
                                            # all this class fundamental info.
        self.null = null
        
    def give_me_sheet_names(self):
        """
        Return the list of names of all sheets in this object.
        """
        return self.me.keys()               # Return the keys (names of sheets) from this class dictionary.
        
    def give_me_variable_names(self,sheet_name):
        """
        Returns the list of variables names in the given sheet name. If sheet
        name does not exist than return empty list.
        """
        if sheet_name in self.me.keys():
            return self.me[sheet_name].keys()  # Return the keys (variables names) from the given sheet (if exists).
        else:
            print 'WARNING: Sheet name ', sheet_name,' does not exist in this object.'   # I'm printing the warning but this may not be useful for integration.
            return []                                                                    # Returns empty list if sheet does not exist.        
    
    def build_me_data_object(self,sheet,names):
        """
        Function to build a data object from variables (list,names) of a specific
        sheet (string). This function will return a data object.
        """
        if type(names)!=type([]):
            return self.error(names,' is not list of existing strings variables.')
        if len(names)<1:
            return self.error(names,' is an empty list. It should be a list of existing string variables.')
        if type(sheet)!=type(''):
            return self.error(sheet,' is not a string with the name of the sheet from which to build an object.')
        if sheet not in self.me.keys():
            return self.error(sheet,' does not exist in sheet names list.')
        flag = False
        counter = 0
        for i in names:
            if i in self.me[sheet].keys():                  # I'm making sure that at least one variable exists on sheet.
                start = self.me[sheet][i][:,np.newaxis]     # And if so, starting to create my final return object.
                header = [i]                
                flag = True
                break
            counter = counter + 1
        if not flag:
            return self.error(names,' does not have any valid entries. At least one entry must be valid to create an array object.')
        c = 0
        for i in names:
            if c>counter:
                if i in self.me[sheet].keys():
                    start = np.hstack((start,self.me[sheet][i][:,np.newaxis]))  # Horizontal stacking to all names accepted.
                    header.append(i)
        return dataObject(start,header)  # Returns a specific kind of data object.
        
    def build_me_point_object(self,sheet,names,x,y,z=None):
        """
        Function to build a point object from variables (list,names) of a specific
        sheet (string). The user must also give the variables strings to x,y and
        z (default is z==None) coordinate variables. Notice that the names list
        should have no coordinates strings names (unless you want them as
        variables).
        """
        if type(names)!=type([]):
            return self.error(names,' is not list of existing strings variables.')
        if len(names)<1:
            return self.error(names,' is an empty list. It should be a list of existing string variables.')
        if type(sheet)!=type(''):
            return self.error(sheet,' is not a string with the name of the sheet from which to build an object.')
        if sheet not in self.me.keys():
            return self.error(sheet,' does not exist in sheet names list.')
        if type(x)!=type(''):
            return self.error(x,' is no a string with the name of the x coordinate variable.')
        if x not in self.me[sheet].keys():
            return self.error(x,' does not exist in the sheet variables names.')
        if type(y)!=type(''):
            return self.error(y,' is no a string with the name of the y coordinate variable.')
        if y not in self.me[sheet].keys():
            return self.error(y,' does not exist in the sheet variables names.')
        if z!=None:
            if type(z)!=type(''):
                return self.error(z,' is no a string with the name of the z coordinate variable.')
            if z not in self.me[sheet].keys():
                return self.error(z,' does not exist in the sheet variables names.')
        flag = False
        counter = 0
        for i in names:
            if i in self.me[sheet].keys():                  # I'm making sure that at least one variable exists on sheet.              
                start = self.me[sheet][i][:,np.newaxis]     # And if so, starting to create my final return object.
                header = [i]                  
                flag = True
                break
            counter = counter + 1
        if not flag:
            return self.error(names,' does not have any valid entries. At least one entry must be valid to create an array object.')
        xa = self.me[sheet][x]
        ya = self.me[sheet][y]
        if z!=None: za = self.me[sheet][z]
        else: za = None
        c = 0
        for i in names:
            if c>counter:
                if i in self.me[sheet].keys():
                    start = np.hstack((start,self.me[sheet][i][:,np.newaxis]))  # Horizontal stacking to all names accepted.
                    header.append(i)
        return pointObject(xa,ya,za,start,header)
                
    def error(what,say):
        """
        General function to print an error. Just give the object that failed and
        the message it's suppose to appear next (what, say). It will appear as
        ERROR: what say.
        """
        print 'ERROR: ', what, say
