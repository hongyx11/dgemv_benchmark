
#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import seaborn as sns
import sys
#%%
def extractfile(filename):
  resmap = {}
  with open(filename, 'r') as f:
    f.readline()
    resmap['M'] = int(f.readline().strip('\n'))
    f.readline()
    resmap['N'] = int(f.readline().strip('\n'))
    f.readline()
    resmap['pres'] = f.readline().strip('\n')
    f.readline()
    fplist = f.readline().strip('\n').split(' ')
    resmap['flops_gbs'] = [float(x) for x in fplist]
    f.readline()
    relist = f.readline().strip('\n').split(' ')
    resmap['relerr'] = [float(x) for x in relist]
    f.readline()
    bdlist = f.readline().strip('\n').split(' ')
    resmap['bd'] = [float(x) for x in bdlist]
    f.readline()
    resmap['exptype'] = f.readline().strip('\n')
    return resmap


def addmaptodf(df, resmap):
  if df.empty:
    df = pd.DataFrame({'M':[],'N':[],'pres':[],'flops_gbs':[],'relerr':[],'exptype':[]})
  for i in range(len(resmap['flops_gbs'])):
    m = resmap['M']
    n = resmap['N']
    pres = resmap['pres']
    exptype = resmap['exptype']
    newrow = {'M':m,'N':n,'pres':pres,'flops_gbs':resmap['flops_gbs'][i],
    'relerr':resmap['relerr'][i],'exptype':exptype}
    df = df.append(newrow,ignore_index=True)
  return df

def boxplot(df, exptype,c='r'):

  spidx = (df.pres == 'single') & (df.exptype == exptype)
  dpidx = (df.pres == 'double') & (df.exptype == exptype)
  ax = sns.boxplot(x='N', y='flops_gbs', data=df[spidx],fliersize=1,width=0.2)
  singlefpmean = df[spidx].groupby('N').mean().flops_gbs.to_numpy()
  plt.plot(singlefpmean,label='SP,'+exptype,color=c,linestyle='-')
  ax = sns.boxplot(x='N', y='flops_gbs', data=df[dpidx],fliersize=1,width=0.2)
  doublefpmean = df[dpidx].groupby('N').mean().flops_gbs.to_numpy()
  plt.plot(doublefpmean,label='DP,'+exptype,color=c, linestyle='--')
  return ax



def baseplot(df, exptypes):
  plt.figure(figsize=(4,3),dpi=150)
  c=['r','g','b']
  for idx,exp in enumerate(exptypes):
    if exp in set(df.exptype):
      ax = boxplot(df,exp,c[idx])
  ax.xaxis.set_tick_params(labelsize=8)
  ax.yaxis.set_tick_params(labelsize=8)
  ax.set_xticklabels(labels=[str(int(x)) for x in sorted(set(df.N))])
  plt.grid(True, 'both')
  plt.xlabel("M = N",fontsize=10)
  plt.ylabel("Gflop/s",fontsize=10)
  plt.legend(fontsize=8)
  plt.savefig("plots/{}.pdf".format("-".join(exptypes)),bbox_inches='tight')
  plt.show()

# %%

def plotnvidia():
  df = pd.DataFrame()
  for f in os.listdir('log'):
    if f.endswith('P100.txt') or f.endswith('V100.txt') or f.endswith('A100.txt'):
      resmap = extractfile('log/'+f)
      df = addmaptodf(df, resmap)
  baseplot(df, ['P100','V100'])


def plotamd():
  pass


def plotintel():
  pass




# %%

"""
plt.figure(figsize=(4,3),dpi=150)
ax = boxplot('V100')
# ax = boxplot('P100')
ax.xaxis.set_tick_params(labelsize=8)
ax.yaxis.set_tick_params(labelsize=8)
ax.set_xticklabels(labels=[str(int(x)) for x in sorted(set(df.N))])
plt.grid(True, 'both')
plt.xlabel("M = N",fontsize=10)
plt.ylabel("Gflop/s",fontsize=10)
plt.legend(fontsize=8)
plt.show()
plt.figure(figsize=(4,3),dpi=150)
# ax = boxplot('V100')
ax = boxplot('P100')
ax.xaxis.set_tick_params(labelsize=8)
ax.yaxis.set_tick_params(labelsize=8)
ax.set_xticklabels(labels=[str(int(x)) for x in sorted(set(df.N))])
plt.grid(True, 'both')
plt.xlabel("M = N",fontsize=10)
plt.ylabel("Gflop/s",fontsize=10)
plt.legend(fontsize=8)
plt.show()
"""