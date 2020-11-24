
#%%
import numpy as np
import matplotlib.pyplot as plt
filename = 'V100res.txt'

#%%
def extractfile(filename):
  with open(filename, 'r') as f:
    f.readline()
    while 1:
      line = f.readline()
      if not line:
        break
      linelist = line.strip('\n').split(' ')
      print(linelist)


# %%
extractfile('V100res.txt')
# %%
