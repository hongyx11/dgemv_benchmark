
#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

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
# %%
df = pd.DataFrame()
for f in os.listdir('log'):
  if f.endswith('.txt'):
    resmap = extractfile('log/'+f)
    df = addmaptodf(df, resmap)

# %%
print(df)

# %%
import seaborn as sns
def boxplot(exptype):
  spidx = (df.pres == 'single') & (df.exptype == exptype)
  dpidx = (df.pres == 'double') & (df.exptype == exptype)
  ax = sns.boxplot(x='N', y='flops_gbs', data=df[spidx],fliersize=3)
  singlefpmean = df[spidx].groupby('N').mean().flops_gbs.to_numpy()
  plt.plot(singlefpmean,label='SP,'+exptype)
  ax = sns.boxplot(x='N', y='flops_gbs', data=df[df.pres=='double'],fliersize=3)
  doublefpmean = df[dpidx].groupby('N').mean().flops_gbs.to_numpy()
  plt.plot(doublefpmean,label='DP,'+exptype)
  return ax
# %%
plt.figure(figsize=(4,3),dpi=150)
ax = boxplot('V100')
ax.xaxis.set_tick_params(labelsize=8)
ax.yaxis.set_tick_params(labelsize=8)
ax.set_xticklabels(labels=[str(int(x)) for x in sorted(set(df.N))])
plt.grid(True, 'both')
plt.xlabel("M = N",fontsize=10)
plt.ylabel("Gflop/s",fontsize=10)
plt.legend(fontsize=8)
plt.show()
# %%
