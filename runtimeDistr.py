from datetime import datetime
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
import math
import subprocess
import sys

def getTime(l):
  startTime = datetime.now()
  subprocess.run('python3 genRSAkey.py '+str(l),stderr=subprocess.STDOUT,shell=True)
  t = datetime.now() - startTime
  return str(t)

if __name__ == "__main__":
  
  t=[]

  # Run prime generation for the specified number of times and register times.
  for i in range(int(sys.argv[2])):
    k = float(str(getTime(sys.argv[1]))[5:15])
    t.append(k)

  # Check the average runtime
  avg = sum(t)/len(t)
  
  print (t)
  print (avg)

  it = []

  # Round the values of t list of times to the nearest integer value for seconds.
  for i in range(math.floor(min(t)),math.ceil(max(t))+1,1):
    count_i=0
    for j in t:
      if (round(j) == i):
        count_i+=1
    it.append((i,count_i))

  # Frequency for k seconds
  kf = [x[1] for x in it]
  # Value of k seconds rounded to nearest int
  kv = [x[0] for x in it]

  # Save graph with the name below + number of times ran.
  figname="LPrimeFreqs"+str(sys.argv[2])

  indices = np.arange(len(it))
  plt.bar(indices,kf,color='b')
  plt.xticks(indices,kv,rotation='vertical')
  plt.tight_layout()
  plt.savefig(figname,pad_inches=0.1)