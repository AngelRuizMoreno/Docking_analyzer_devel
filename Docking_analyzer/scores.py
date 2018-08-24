#Modules to use
import re
import os
import glob
import pandas as pd
import matplotlib as mt
from matplotlib import pyplot as plt

#TO DO:
# - Include the search of positive score values into get_scores funtion
# - Incluide a funtion to find and save GOLD


# NOW TO THE FUNTIONS
class get_scores ():

    def __init__ (self,path=None,docker=None, save_csv=True, sort=True):
        self.path       = path
        self.docker     = docker
        self.save_csv   = save_csv
        self.sort       = sort
        if docker == 'autodockvina':
            os.chdir (path) #Path where *.pdbqt output files are located
            files=[]
            scores=[]
            for file in glob.glob('*.pdbqt'):
                with open(file,'rt') as file:
                    for line in file:
                        line = line.strip()
                        if "VINA RESULT" in line:
                            neg = re.search(r'-\d.\d', line)
                            if neg:
                                files.append (file.name)
                                scores.append (neg.group())
            d={'file':pd.Series(files),'score':pd.Series(scores)}
            print ('Raw score values')
            table=pd.DataFrame (d)
            print (table)

        pass

        if docker== 'gold':
            os.chdir (path) #Path where *.pdbqt output files are located
            files=[]
            scores=[]
            for file in glob.glob('*.mol2'):
                with open(file,'rt') as file:
                    for line in file:
                        line = line.strip()
                        if "<score>" in line:
                            neg = re.search(r'\d\d.\d\d', line)
                            if neg:
                                files.append (file.name)
                                scores.append (neg.group())
            d={'file':pd.Series(files),'score':pd.Series(scores)}
            print ('Raw score values')
            table=pd.DataFrame (d)
            print (table)
        pass

        if sort == True:
            print ('Sorted score values')
            sort=table.sort_values ('score',ascending=False)
            print (sort)
        if save_csv == True:
            table.to_csv ('no_sorted_scores.csv')
            sort.to_csv ('sorted_scores.csv')
