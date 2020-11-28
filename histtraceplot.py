#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import sys
sys.path.append('.')
from module import *
"""
config
"""
instrs = ['SCEXAO','MICADO [1]','MICADO [2]','MAVIS','MAORY','EPICS']
instrs_plt = ['SCEXAO','MICADO1','MICADO2','MAVIS','MAORY','EPICS']
labeltype = ['Intel Cascade Lake','NEC SX-Aurora 20B','NVIDIA A100 40GB']
mnlist = [[2000,14000],[5000,10000],[5000,25000],[5000,20000],\
          [8000,80000],[35000,70000]]
exptypes = ['cascadelake','NEC_20B','a100']
searchfolder = 'log'

if not os.path.exists('plots'):
    os.makedirs('plots')

if not os.path.exists('plots/seperate_trace'):
    os.makedirs('plots/seperate_trace')
if not os.path.exists('plots/merge_trace'):
    os.makedirs('plots/merge_trace')
if not os.path.exists('plots/seperate_hist'):
    os.makedirs('plots/seperate_hist')
if not os.path.exists('plots/merge_hist'):
    os.makedirs('plots/merge_hist')

    
    
df = loaddatafromtxt(mnlist, exptypes, searchfolder)

"""
seperate trace plot 
"""
labeli = 0
for mn in mnlist:
  for exp in exptypes:
    plt.figure(figsize=(4,3),dpi=150)
    tmpdf = selectdata(df, mn[0], mn[1], [exp])
    plt.plot(tmpdf.time.to_numpy()*1e6)
    plt.ylabel('Time(us)')
    plt.xlabel('Nruns')
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.title('{} {} trace'.format(instrs_plt[labeli],exp))
    plt.savefig('plots/seperate_trace/{}_{}_trace.pdf'.format(instrs_plt[labeli], exp),
                bbox_inches='tight')
    plt.close()
  labeli+=1

"""
merge trace plot 
"""
labeli = 0
for mn in mnlist:
  plt.figure(figsize=(4,3),dpi=150)
  for idx,exp in enumerate(exptypes):
    tmpdf = selectdata(df, mn[0], mn[1], [exp])
    plt.plot(tmpdf.time.to_numpy()*1e6,label=labeltype[idx])
  plt.ylabel('Time(us)')
  plt.xlabel('Nruns')
  plt.legend()
  plt.xticks(fontsize=8)
  plt.yticks(fontsize=8)
  plt.title('{} trace merge'.format(instrs_plt[labeli]))
  plt.savefig('plots/merge_trace/{}_trace_merge.pdf'.format(instrs_plt[labeli]),
                bbox_inches='tight')
  plt.close()
  labeli+=1

"""
seperate hist plot 
"""
labeli = 0
for mn in mnlist:
  for exp in exptypes:
    plt.figure(figsize=(4,3),dpi=150)
    tmpdf = selectdata(df, mn[0], mn[1], [exp])
    plt.hist(tmpdf.time.to_numpy()*1e6, bins=100)
    plt.ylabel('Occurance')
    plt.xlabel('Time(us)')
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.title('{} {} hist'.format(instrs_plt[labeli],exp))
    plt.savefig('plots/seperate_hist/{}_{}_hist.pdf'.format(instrs_plt[labeli], exp),
                bbox_inches='tight')
    plt.close()
  labeli+=1

"""
merge hist plot 
"""
labeli = 0
for mn in mnlist:
  plt.figure(figsize=(4,3),dpi=150)
  ret = []
  for idx,exp in enumerate(exptypes):
    tmpdf = selectdata(df, mn[0], mn[1], [exp])
    ret.append( (tmpdf.time.to_numpy()*1e6).tolist() )
  plt.hist(ret,label=labeltype,bins=100)
  plt.ylabel('Occurance')
  plt.xlabel('Time(us)')
  plt.legend()
  plt.xticks(fontsize=8)
  plt.yticks(fontsize=8)
  plt.title('{} histogram'.format(instrs_plt[labeli]))
  plt.savefig('plots/merge_hist/{}_hist_merge.pdf'.format(instrs_plt[labeli]),
                bbox_inches='tight')
  plt.close()
  labeli+=1
