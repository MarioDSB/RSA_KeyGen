from datetime import datetime
import subprocess
import sys

def getTime(l):
  out = subprocess.check_output('python3 genPrime.py '+str(l),stderr=subprocess.STDOUT,shell=True)
  return out

if __name__ == "__main__":
  
  t=[]

  for i in range(int(sys.argv[2])):
    k = float(str(getTime(sys.argv[1]))[7:16])
    t.append(k)


  avg = sum(t)/len(t)
  
  print (t)
  print (avg)