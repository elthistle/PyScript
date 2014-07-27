#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import csv
import os

def theApp():
    # define constants here
    path_to_folder = sys.argv[1] # assuming th user is smart enough to pass the argument
    
    # here comes the code
    for fname in os.listdir(path_to_folder):
        if not fname.endswith('.csv'): continue
        fullname = os.path.join(put_k_papke, fname)
        
        # now we handle the file (we know it as fname or fullname)
        output = "results go here!"
        
        # time to output!
        print "{0}; {1}".format(fname, output)

if __name__ == "__main__":
    theApp()
