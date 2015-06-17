# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:03:35 2015

@author: pedro.correia
"""

from __future__ import division  # Just making sure that correct integer division is working
import numpy as np               # This is numpy,python numerical library
import xlrd as xcl               # This library allow you to manipulate (read and write) excel files
import cPickle as pickle         # Library used to save and load dictionaries
import objects_parser as obj     # Our local objects library.

def __open_excel_book__(path):
    """
    NOTE: internal function. Use open_excel_file function.
    User gives a string path and this function returns the open excel book.
    """
    book = xcl.open_workbook(path,on_demand=True)
    return book
    
def __array_by_type__(sheet,col,null=-999):
    """
    NOTE: internal function. Use open_excel_file function.
    This function receives sheet and column number and returns an array with the
    correct type. The null is by default -999 but you can change it on the third
    argument.
    """
    try:
        float(sheet.cell_value(1, col))
        return np.zeros(sheet.nrows,dtype=type(sheet.cell_value(1, col))),null
    except ValueError:
        return np.zeros(sheet.nrows,dtype='|S15'),str(null) #type(sheet.cell_value(1, col))),str(null)
    
def __build_excel_dictionary__(book,null=-999):
    """
    NOTE: internal function. Use open_excel_file function.
    Function that receives an excel book (see: __open_excel_book__) and extracts to
    dictionaries (with numpy arrays) all information from the excel book. Empty
    cells are given the null value (default is -999).
    """
    sheet_dictionary = {}
    for name in book.sheet_names():
        sheet = book.sheet_by_name(name)
        local_dictionary = {}
        for col in xrange(sheet.ncols):
            local_array,null = __array_by_type__(sheet,col,null)
            for row in xrange(1,sheet.nrows):
                if sheet.cell_type(row, col) in (xcl.XL_CELL_EMPTY, xcl.XL_CELL_BLANK):
                    local_array[row] = null
                else:
                    local_array[row] = sheet.cell_value(row, col)
            local_dictionary[sheet.cell_value(0, col)] = local_array
        sheet_dictionary[name] = local_dictionary
    return sheet_dictionary
    
def open_excel_file(path,null=-999):
    """
    Function that opens excel file into a excel_class_object and return the
    last.
    """
    book = __open_excel_book__(path)
    data = obj.excelObject(__build_excel_dictionary__(book,null),null)
    return data
    
def save_excel_object(path,obj):
    """
    Saves excel object to file. Give path and excel object.
    """
    with open(path, 'wb') as outfile:
        pickle.dump(obj.me, outfile, protocol=pickle.HIGHEST_PROTOCOL)
        
def open_excel_object(path,null=-999):
    """
    Creates an excel object from epy (pickle) loaded file.
    """
    return obj.excelObject(pickle.load(open(path, "rb" )),null)
