# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 12:51:31 2021

@author: JUCA
"""

import os
from os import listdir
from os.path import isfile, join
import pandas as pd


dirName = 'UPDATE'
#C:/Users/juca/AWS


filesList = [f for f in listdir(dirName) if isfile(join(dirName, f))]

listOfFile = os.listdir(dirName)

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
        
    return allFiles

files = getListOfFiles(dirName)

df = pd.DataFrame(files, columns=['full_path'])
df['file_name'] = df.full_path.str.split('\\').str[-1]
df['file_type'] = df.file_name.str.split('.').str[-1]
#df['relative_path'] = df['full_path'].str[dirName:]

print('Done')