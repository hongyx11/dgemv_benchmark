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
instrs_plt = ['SCEXAO','MICADO1','MICADO2','MAVIS','MAORY','EPICS']
labeltype = ['AMD Epyc Rome','Intel Cascade Lake','NEC SX-Aurora','NVIDIA A100']

if not os.path.exists('plots'):
    os.makedirs('plots')

if not os.path.exists('plots/speedup'):
    os.makedirs('plots/speedup')

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

transpose='Notrans'
searchfolder = 'log'
precision = 'double'
exptypes = ['a100']

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

medianlist = []
for k,v in mnlist:
  tmpdf = selectdata(df,k,v,['a100'])
  medianlist.append(np.median(tmpdf.time.to_numpy()))

for instridx in range(6):
  fig, ax1 = plt.subplots()
  color = 'tab:green'
  ax1.set_xlabel('# of GPUs')
  ret = medianlist[instridx*4:(instridx+1)*4]
  ret.reverse()
  ret = np.array(ret)
  ret = ret[0] / ret
  ax1.set_ylabel('Speed up', color='green', fontsize=14)
  ax1.tick_params(axis='y', labelcolor='green')
  plt.plot([1,2,4,8],linestyle='dashed',label='ideal speed up',marker='.')
  plt.plot(ret,marker='x')
  ax1.set_facecolor('lightgrey')
  ax1.set_alpha(0.0001)
  xtick = ['1','2','4','8']
  plt.grid(which='both', color='white', linewidth='0.3')
  plt.xlabel("# of GPUs", fontsize=14)
  plt.title('NVIDIA A100 speed up on {} '.format(instrs[instridx]))
  plt.xticks(range(len(xtick)), xtick,fontsize=12)
  plt.savefig('plots/speedup/speedup_a100_{}.pdf'.format(instrs_plt[instridx]))
plt.show()