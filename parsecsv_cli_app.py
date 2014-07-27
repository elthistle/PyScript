#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import csv
import os

class CLIApp(object):

    def showUsage(self):
        print "How to use this script: ./cli_app.py put_k_papke"

    def parsniPapku(self, put_k_papke):
        for fname in os.listdir(put_k_papke):
            if not fname.endswith('.csv'): continue
            fullname = os.path.join(put_k_papke, fname)
            print "{0}; {1}".format(fname, self.parseMyFile(fullname))

    def parseMyFile(self, fname):
        output = []
        fh = open(fname, 'rb')
	csvshechka = csv.reader(fh)
        for row in csvshechka:
            chislo = 0
            try:
                chislo = int(row[126])
            except:
                pass
            if chislo > 0:
                if 'S' in row[98]:
                    chislo += 300
                output.append(str(chislo))
        fh.close()
        return "; ".join(output)

    def __init__(self):
        if len(sys.argv) < 2:
	    self.showUsage();
        else:
            print self.parsniPapku(sys.argv[1])

if __name__ == "__main__":
    CLIApp()
