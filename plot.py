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

#%%
def extractfile(filename):
  resmap = {}
  with open(filename, 'r') as f:
    f.readline()
    m = int(f.readline().strip('\n'))
    f.readline()
    n = int(f.readline().strip('\n'))
    f.readline()
    pres = f.readline().strip('\n')
    f.readline()
    fplist = f.readline().strip('\n').split(' ')
    resmap['time'] = [float(x) for x in fplist]
    f.readline()
    relist = f.readline().strip('\n').split(' ')
    resmap['relerr'] = [float(x) for x in relist]
    f.readline()
    bdlist = f.readline().strip('\n').split(' ')
    resmap['bandwidth'] = [float(x) for x in bdlist]
    f.readline()
    exptype = f.readline().strip('\n')
    nruns = len(resmap['bandwidth'])
    resmap['M'] = [m for _ in range(nruns)]    
    resmap['N'] = [n for _ in range(nruns)]
    resmap['pres'] = [pres for _ in range(nruns)]
    resmap['exptype'] = [exptype for _ in range(nruns)]
  df = pd.DataFrame.from_dict(resmap)
  return df

def getboxplottimeinput(df, exptypes):
  ret = []
  for exp in exptypes:
    ret.append(df[df.exptype == exp].time.to_numpy().tolist())
  return ret

def bandwidthplot(df, mnlist, exptypes, precision='double'):
  bardata = [[] for _ in range(len(exptypes))]
  for idx,exp in enumerate(exptypes):
    for mnidx in range(len(mnlist)):
      dataidx = (df.pres == precision) & (df.exptype == exp) & \
        (df.M == mnlist[mnidx][0]) & (df.N == mnlist[mnidx][1])
      tmpdf = df[dataidx]
      bardata[idx].append(tmpdf.bandwidth.median())
#   plt.figure(figsize=(4,3),dpi=150)
  fig, ax = plt.subplots()
  ax.set_facecolor('lightgrey')
  ax.set_alpha(0.0001)
  x_11 =[i for i in range(len(mnlist))] 

  x_21 =[i-.1 for i in range(len(mnlist))] 
  x_22 =[i+.1 for i in range(len(mnlist))] 

  x_31 =[i-.2 for i in range(len(mnlist))]
  x_32 =[i for i in range(len(mnlist))]
  x_33 =[i+.2 for i in range(len(mnlist))]

  x_41 =[i-.3 for i in range(len(mnlist))]
  x_42 =[i-.1 for i in range(len(mnlist))]
  x_43 =[i+.1 for i in range(len(mnlist))]
  x_44 =[i+.3 for i in range(len(mnlist))]
  colors = ['orange','blue','darkgreen','magenta']
  if len(exptypes) == 1:
    ax.bar(x_11, bardata[0], color=colors[0],  
           width=0.2, label='{}'.format(exptypes[0]))
  elif len(exptypes) == 2:
    ax.bar(x_21, bardata[0], color=colors[0],  
           width=0.2, label='{}'.format(labeltype[0]))
    ax.bar(x_22, bardata[1], color=colors[1],  
           width=0.2, label='{}'.format(labeltype[1]))
    plt.xticks([i for i in range(len(mnlist))],instrs,fontsize=10)

  elif len(exptypes) == 3:
    ax.bar(x_31, bardata[0], color=colors[0],  
           width=0.2, label='{}'.format(exptypes[0]))
    ax.bar(x_32, bardata[1], color=colors[1],  
           width=0.2, label='{}'.format(exptypes[1]))
    ax.bar(x_33, bardata[2], color=colors[2],  
           width=0.2, label='{}'.format(exptypes[2]))
    plt.xticks([i for i in range(len(mnlist))],instrs,fontsize=10)

  elif len(exptypes) == 4:
    ax.bar(x_41, bardata[0], color=colors[0],  
           width=0.2, label='{}'.format(labeltype[0]))
    ax.bar(x_42, bardata[1], color=colors[1],  
           width=0.2, label='{}'.format(labeltype[1]))
    ax.bar(x_43, bardata[2], color=colors[2],  
           width=0.2, label='{}'.format(labeltype[2]))
    ax.bar(x_44, bardata[3], color=colors[3],  
           width=0.2, label='{}'.format(labeltype[3]))
    plt.xticks([i for i in range(len(mnlist))],instrs,fontsize=10)

  else:
    print('no suitable exptypes length')
    exit()
#   plt.tight_layout()
  plt.xlabel("Intruments",fontsize=12)
  plt.ylabel("Bandwidth (GB/s)",fontsize=12)

  plt.legend(loc='upper left')
  plt.minorticks_on()
  plt.grid(which='both', color='white', linewidth='0.3')
  plt.savefig('Bandwidth_{}.pdf'.format(precision),bbox_inches='tight')

def timeplot(df, mnlist, exptypes, precision='double'):
#   plt.figure(figsize=(4,3),dpi=150)
  fig,ax = plt.subplots()
  ax.set_facecolor('lightgrey')
  ax.set_alpha(0.0001)
  x_11 =[2*i for i in range(len(mnlist))]
  p_1 = np.array(x_11).T

  x_21 =[2*i-.15 for i in range(len(mnlist))] 
  x_22 =[2*i+.15 for i in range(len(mnlist))] 
  p_2 = np.array([x_21,x_22]).T

  x_31 =[2*i-.3 for i in range(len(mnlist))]
  x_32 =[2*i for i in range(len(mnlist))]
  x_33 =[2*i+.3 for i in range(len(mnlist))]
  p3 = np.array([x_31,x_32,x_33]).T

  x_41 =[2*i-.45 for i in range(len(mnlist))]
  x_42 =[2*i-.15 for i in range(len(mnlist))]
  x_43 =[2*i+.15 for i in range(len(mnlist))]
  x_44 =[2*i+.45 for i in range(len(mnlist))]
  p_4 = np.array([x_41,x_42,x_43,x_44]).T
  colors = ['orange','blue','darkgreen','magenta']
  for i in range(len(mnlist)):
    selectidx = (df.M == mnlist[i][0]) & (df.N == mnlist[i][1]) \
    & (df.pres == precision)
    tmpdf = df[selectidx]
    bxtimeip = getboxplottimeinput(tmpdf,exptypes)
    if len(exptypes) == 1:
      pass
    elif len(exptypes) == 2:
      bp = plt.boxplot(bxtimeip,positions = p_2[i], widths = 0.3)
      plt.yscale('log')
      j=0
      for idx,b in enumerate(bp['boxes']):
        b.set_color(colors[j%len(exptypes)])
        bp['medians'][idx].set_color(colors[j%len(exptypes)])
        j+=1
    elif len(exptypes) == 3:
      pass
    elif len(exptypes) == 4:
      bp = plt.boxplot(bxtimeip,positions = p_4[i], widths = 0.2)
      plt.yscale('log')
      j=0
      for idx,b in enumerate(bp['boxes']):
        b.set_color(colors[j%len(exptypes)])
        bp['medians'][idx].set_color(colors[j%len(exptypes)])
        j+=1
  # after for loop
  j=0
  for b in bp['boxes']:
    if j < len(exptypes):
      b.set_label(labeltype[j])
      j += 1

  xtick = instrs
  plt.xticks([2*i for i in range(len(mnlist))],xtick,fontsize=10)
#   plt.tight_layout()
  plt.xlabel("Instruments",fontsize=12)
  plt.ylabel("Time(s)",fontsize=12)
  plt.legend()
  plt.minorticks_on()
  plt.grid(which='both', color='white', linewidth='0.3')
  plt.savefig('Time_{}.pdf'.format(precision),bbox_inches='tight')

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
