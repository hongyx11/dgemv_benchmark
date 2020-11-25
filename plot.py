
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
  for i in range(len(resmap['time'])):
    m = resmap['M']
    n = resmap['N']
    pres = resmap['pres']
    time = resmap['time'][i]
    exptype = resmap['exptype']
    bd = resmap['bd'][i]
    newrow = {'M':m,'N':n,'pres':pres,'time': time,
    'relerr':resmap['relerr'][i],'bandwith':bd,'exptype':exptype}
    df = df.append(newrow,ignore_index=True)
  return df


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

def basebandplot(df, mnlist, exptypes, pres='double'):
  # bandplot is a bar plot!
  # first get mean bandwith
  bardata = [[] for _ in range(len(exptypes))]
  for idx,exp in enumerate(exptypes):
    for mnidx in range(len(mnlist)):
      dataidx = (df.pres == pres) & (df.exptype == exp) & \
        (df.M == mnlist[mnidx][0]) & (df.N == mnlist[mnidx][1])
      tmpdf = df[dataidx]
      bardata[idx].append(tmpdf.bandwith.median())
  print(bardata)
  # plt.figure(figsize=(4,3),dpi=150)
  # fig, ax = plt.subplots()
  # c=['r','g','b']
  # for idx,exp in enumerate(exptypes):
  #   if exp in set(df.exptype):
  #     print('ploting ',exp)
  #     ax = bandplot(df,exp,c[idx])
  # ax.xaxis.set_tick_params(labelsize=8)
  # ax.yaxis.set_tick_params(labelsize=8)
  # ax.set_xticklabels(labels=[str(int(x)) for x in sorted(set(df.N))])
  # plt.grid(True, 'both')
  # plt.xlabel("M = N",fontsize=10)
  # plt.ylabel("Bandwith(GB/s)",fontsize=10)
  # plt.legend(fontsize=7)
  # plt.savefig("plots/{}_bandwith.pdf".format("-".join(exptypes)),bbox_inches='tight')
  # plt.show()



# %%

# def plotnvidia(exptypes):
#   df = pd.DataFrame()
#   for f in os.listdir('log'):
#     for ep in exptypes:
#       if f.endswith(ep+'.txt'):
#         resmap = extractfile('log/'+f)
#         df = addmaptodf(df, resmap)
#   baseplot(df, ['P100','V100'])
#   basetmplot(df,['P100','V100'])
#   basebandplot(df, ['P100','V100'])

# def plotamd():
#   pass


# def plotintel(exptypes):
#   df = pd.DataFrame()
#   for f in os.listdir('log'):
#     for ep in exptypes:
#       if f.endswith(ep + '.txt'):
#         resmap = extractfile('log/'+f)
#         df = addmaptodf(df, resmap)
#   baseplot(df, exptypes)
#   basetmplot(df,exptypes)

# plotnvidia(['P100','V100'])


transpose = sys.argv[1]
if transpose == 'Notrans':
  mnlist = [[5000,10000],[5000,20000], \
  [5000,25000],[8000,80000]]
else:
  mnlist = [[10000,5000],[20000,5000], \
  [25000,5000],[80000,8000]]

searchfolder = sys.argv[2]

precision = sys.argv[3]

exptypes = sys.argv[4:]

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
        resmap = extractfile(fpath)
        df = addmaptodf(df, resmap)
for exp in exptypes:
  if exp not in set(df.exptype):
    print("we have not results for ", exp, ", please check and relaunch.")
    exit()
basebandplot(df, mnlist, exptypes, precision)


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