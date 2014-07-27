#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import csv
import os

def theApp():
    # define constants here
    path_to_folder = sys.argv[1] # assuming th user is smart enough to pass the argument
    column_reaction_time = 126
    column_correct_response = 42
    
    # here comes the code
    for fname in os.listdir(path_to_folder):
        if not fname.endswith('.csv'): continue
        fullname = os.path.join(put_k_papke, fname)
        
        # now we handle the file (we know it as fname or fullname)
        output_cells = []
        fh = open(fullname, 'rb') # opening .csv file
        csv_reader = csv.reader(fh) # reading csv
        for row in csv_reader:
            
            # here we handle the row
            # WARNING: if your .csv contains text entries (like headers) handle them here
            reaction_time = int(row[column_reaction_time]) # here we get the raw RT as a number
            # altering of RT should hppen here
            cell_text = str(chislo) # saving the RT as text for output
            if '0' in row[column_correct_response]: # describe what happens if response is wrong below
                cellText = ' ' # replace reaction time value with nothing (write empty cell)
                
            output_cells.append(cell_text) # saving the final value to output stream
            
        fh.close() # closing .csv file
        
        # time to output!
        output_text = "; ".join(output_cells)
        print "{0}; {1}".format(fname, output_text)

if __name__ == "__main__":
    theApp()
