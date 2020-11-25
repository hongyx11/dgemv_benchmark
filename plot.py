
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
    resmap['time'] = [float(x) for x in fplist]
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
    df = pd.DataFrame({'M':[],'N':[],'pres':[],'flops_gbs':[],
    'relerr':[],'bandwith':[],'exptype':[]})
  for i in range(len(resmap['flops_gbs'])):
    m = resmap['M']
    n = resmap['N']
    pres = resmap['pres']
    exptype = resmap['exptype']
    fps = resmap['flops_gbs'][i]
    abstime = (2.0 * m * n + 3 * m) / (fps * 1.0e9)
    bd = resmap['bd'][i]
    newrow = {'M':m,'N':n,'pres':pres,'flops_gbs': fps,
    'relerr':resmap['relerr'][i],'bandwith':bd,'exptype':exptype}
    df = df.append(newrow,ignore_index=True)
  return df

# def boxplot(df, exptype,c='r'):
#   spidx = (df.pres == 'single') & (df.exptype == exptype)
#   dpidx = (df.pres == 'double') & (df.exptype == exptype)
#   ax = sns.boxplot(x='N', y='flops_gbs', data=df[spidx],fliersize=1,width=0.2,color='skyblue')
#   singlefpmean = df[spidx].groupby('N').median().flops_gbs.to_numpy()
#   plt.plot(singlefpmean,label='SP,'+exptype,color=c,linestyle='-',marker='.')
#   ax = sns.boxplot(x='N', y='flops_gbs', data=df[dpidx],fliersize=1,width=0.2,color='magenta')
#   doublefpmean = df[dpidx].groupby('N').median().flops_gbs.to_numpy()
#   plt.plot(doublefpmean,label='DP,'+exptype,color=c, linestyle='--',marker='.')
#   return ax

# def baseplot(df, exptypes):
#   plt.figure(figsize=(4,3),dpi=150)
#   c=['r','g','b']
#   for idx,exp in enumerate(exptypes):
#     if exp in set(df.exptype):
#       print('ploting ',exp)
#       ax = boxplot(df,exp,c[idx])
#   ax.xaxis.set_tick_params(labelsize=8)
#   ax.yaxis.set_tick_params(labelsize=8)
#   ax.set_xticklabels(labels=[str(int(x)) for x in sorted(set(df.N))])
#   plt.grid(True, 'both')
#   plt.xlabel("M = N",fontsize=10)
#   plt.ylabel("Gflop/s",fontsize=10)
#   plt.legend(fontsize=7)
#   plt.savefig("plots/{}_gflops.pdf".format("-".join(exptypes)),bbox_inches='tight')
#   plt.show()


def timeplot(df, exptype,c='r'):
  spidx = (df.pres == 'single') & (df.exptype == exptype)
  dpidx = (df.pres == 'double') & (df.exptype == exptype)
  ax = sns.boxplot(x='N', y='abstime', data=df[spidx],fliersize=1,width=0.2,color='skyblue')
  singlefpmean = df[spidx].groupby('N').median().abstime.to_numpy()
  plt.plot(singlefpmean,label='SP,'+exptype,color=c,linestyle='-',marker='.')
  ax = sns.boxplot(x='N', y='abstime', data=df[dpidx],fliersize=1,width=0.2,color='magenta')
  doublefpmean = df[dpidx].groupby('N').median().abstime.to_numpy()
  plt.plot(doublefpmean,label='DP,'+exptype,color=c, linestyle='--',marker='.')
  return ax

def basetmplot(df, exptypes):
  plt.figure(figsize=(4,3),dpi=150)
  c=['r','g','b']
  for idx,exp in enumerate(exptypes):
    if exp in set(df.exptype):
      print('ploting ',exp)
      ax = timeplot(df,exp,c[idx])
  ax.xaxis.set_tick_params(labelsize=8)
  ax.yaxis.set_tick_params(labelsize=8)
  ax.set_xticklabels(labels=[str(int(x)) for x in sorted(set(df.N))])
  plt.grid(True, 'both')
  plt.xlabel("M = N",fontsize=10)
  plt.ylabel("Time(s)",fontsize=10)
  plt.legend(fontsize=7)
  plt.yscale('log')
  plt.savefig("plots/{}_time.pdf".format("-".join(exptypes)),bbox_inches='tight')
  plt.show()


def bandplot(df, exptype,c='r'):
  spidx = (df.pres == 'single') & (df.exptype == exptype)
  dpidx = (df.pres == 'double') & (df.exptype == exptype)
  ax = sns.boxplot(x='N', y='bandwith', data=df[spidx],fliersize=1,width=0.2,color='skyblue')
  singlefpmean = df[spidx].groupby('N').median().bandwith.to_numpy()
  plt.plot(singlefpmean,label='SP,'+exptype,color=c,linestyle='-',marker='.')
  ax = sns.boxplot(x='N', y='bandwith', data=df[dpidx],fliersize=1,width=0.2,color='magenta')
  doublefpmean = df[dpidx].groupby('N').median().bandwith.to_numpy()
  plt.plot(doublefpmean,label='DP,'+exptype,color=c, linestyle='--',marker='.')
  return ax

def basebandplot(df, exptypes):
  plt.figure(figsize=(4,3),dpi=150)
  c=['r','g','b']
  for idx,exp in enumerate(exptypes):
    if exp in set(df.exptype):
      print('ploting ',exp)
      ax = bandplot(df,exp,c[idx])
  ax.xaxis.set_tick_params(labelsize=8)
  ax.yaxis.set_tick_params(labelsize=8)
  ax.set_xticklabels(labels=[str(int(x)) for x in sorted(set(df.N))])
  plt.grid(True, 'both')
  plt.xlabel("M = N",fontsize=10)
  plt.ylabel("Bandwith(GB/s)",fontsize=10)
  plt.legend(fontsize=7)
  plt.savefig("plots/{}_bandwith.pdf".format("-".join(exptypes)),bbox_inches='tight')
  plt.show()


#%%



# %%

def plotnvidia(exptypes):
  df = pd.DataFrame()
  for f in os.listdir('log'):
    for ep in exptypes:
      if f.endswith(ep+'.txt'):
        resmap = extractfile('log/'+f)
        df = addmaptodf(df, resmap)
  baseplot(df, ['P100','V100'])
  basetmplot(df,['P100','V100'])
  basebandplot(df, ['P100','V100'])

def plotamd():
  pass


def plotintel(exptypes):
  df = pd.DataFrame()
  for f in os.listdir('log'):
    for ep in exptypes:
      if f.endswith(ep + '.txt'):
        resmap = extractfile('log/'+f)
        df = addmaptodf(df, resmap)
  baseplot(df, exptypes)
  basetmplot(df,exptypes)


# plotnvidia(['P100','V100'])

vendor = sys.argv[1]
exptypes = sys.argv[2:]
print("genrating plots for ", vendor)

print("exptype is ", exptypes)

if vendor == 'intel':
  plotintel(exptypes)
elif vendor == 'amd':
  plotamd(exptypes)
elif vendor == 'nvidia':
  plotnvidia(exptypes)

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