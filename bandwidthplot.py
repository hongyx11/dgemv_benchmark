#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys
sys.path.append('.')
from module import *
"""
global variable
"""
instrs = ['SCEXAO','MICADO [1]','MICADO [2]','MAVIS','MAORY','EPICS']
labeltype = ['AMD Epyc Rome','Intel Cascade Lake','NEC SX-Aurora 20B','NVIDIA A100 40GB']

# these are the dimension we are lookging into
# it matches the order of instrs, ['SCEXAO','MICADO [1]','MICADO [2]','MAVIS','MAORY','EPICS']
mnlist = [[2000,10000],[5000,10000],[5000,25000],[5000,20000],[8000,80000],[35000,70000]]  
searchfolder = 'log'
precision = 'double'
exptypes = ['amd','cascadelake','NEC_20B','a100']

print("genrating dimension size: ", mnlist)
print("searching folder: ", searchfolder)
print("precision: ", precision)
print("exptypes: ", exptypes)
df = loaddatafromtxt(mnlist, exptypes, searchfolder)

if not os.path.exists('plots'):
    os.makedirs('plots')

if not os.path.exists('plots/bandwidth'):
    os.makedirs('plots/bandwidth')

bandwidthplot(df, mnlist, exptypes,labeltype,instrs)
timeplot(df, mnlist, exptypes,labeltype, instrs)
plt.show()
