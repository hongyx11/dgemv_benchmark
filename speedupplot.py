#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys

"""
global variable
"""
instrs = ['SCEXAO','MICADO [1]','MICADO [2]','MAVIS','MAORY','EPICS']
labeltype = ['AMD Epyc Rome','Intel Cascade Lake','NEC SX-Aurora','NVIDIA A100']

transpose = 'Notrans'
if transpose == 'Notrans':
  mnlist = [[2000,14000],[5000,10000],[5000,25000],[5000,20000] \
  ,[8000,80000],[35000,70000]]
else:
  mnlist = [[14000,2000],[10000,5000],[25000,5000],[20000,5000]\
  ,[80000,8000],[70000,35000]]
mnlist = [
  [250,14000],
  [500,14000],
  [1000,14000],
  [2000,14000],
  [625,10000],
  [1250,10000],
  [2500,10000],
  [5000,10000],
  [625,25000],
  [1250,25000],
  [2500,25000],
  [5000,25000],
  [625,20000],
  [1250,20000],
  [2500,20000],
  [5000,20000],
  [1000,80000],
  [2000,80000],
  [4000,80000],
  [8000,80000],
  [4375,70000],
  [8750,70000],
  [17500,70000],
  [35000,70000]
]

searchfolder = '/Users/hongy0a/tmplog/dgemv_benchmark/log'
precision = 'double'
exptypes = ['amd','cascadelake','nec','a100']

print("genrating plots for ", transpose, " mnlist ", mnlist)
print("searching folder: ", searchfolder)
print("precision: ", precision)
assert(precision == 'double' or precision == 'single' or precision == 'all')
print("exptype is ", exptypes)

df = pd.DataFrame()
for k,v in mnlist:
  for exp in exptypes:
    for f in os.listdir(searchfolder):
      if f.endswith(exp+'.txt') and f.startswith("M{}N{}".format(k,v)):
        fpath = searchfolder + '/' + f
        resmapdf = extractfile(fpath)
        df = df.append(resmapdf,ignore_index=True)
for exp in exptypes:
  if exp not in set(df.exptype):
    print("we have not results for ", exp, ", please check and relaunch.")
    exit()