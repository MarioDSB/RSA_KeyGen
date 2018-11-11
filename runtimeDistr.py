from datetime import datetime
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import math
import subprocess
import sys

def getTime(l):
  startTime = datetime.now()
  out = subprocess.check_output('python3 genPrime.py '+str(l),stderr=subprocess.STDOUT,shell=True)
  t = datetime.now() - startTime
  return str(t)

if __name__ == "__main__":
  
  t=[]
  b=[]

  for i in range(int(sys.argv[2])):
    k = float(str(getTime(sys.argv[1]))[5:15])
    if (int(k) not in b):
      b.append(int(k))
    t.append(k)


  avg = sum(t)/len(t)
  
  print (t)
  print (avg)

  bns = list(range(0,math.ceil(max(t))+1,1))

  figname="LPrimeFreqs"+str(sys.argv[2])

  plt.xticks(bns)
  plt.yticks(list(range(0,int(sys.argv[2])+1,1)))
  plt.hist(t, bins=bns)
  plt.savefig(figname,pad_inches=0.1)