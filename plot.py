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

# these are the dimension we are lookging into
# it matches the order of instrs, ['SCEXAO','MICADO [1]','MICADO [2]','MAVIS','MAORY','EPICS']
mnlist = [[2000,10000],[5000,10000],[5000,25000],[5000,20000],[8000,80000],[35000,70000]]  
searchfolder = 'log'
precision = 'double'
exptypes = ['amd','cascadelake','nec','a100']

print("genrating dimension size: ", mnlist)
print("searching folder: ", searchfolder)
print("precision: ", precision)
print("exptypes: ", exptypes)

df = pd.DataFrame()
for k,v in mnlist:
  for exp in exptypes:
    for f in os.listdir(searchfolder):
      if f.endswith(exp+'.txt') and f.startswith("M{}N{}".format(k,v)):
        fpath = searchfolder + '/' + f
        resmapdf = extractfile(fpath)
        df = df.append(resmapdf,ignore_index=True)

bandwidthplot(df, mnlist, exptypes)
timeplot(df, mnlist, exptypes)
plt.show()
