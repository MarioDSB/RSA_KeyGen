from datetime import datetime
import subprocess
import sys

def getTimes(l):
  out = subprocess.check_output('python3 genPrime.py '+str(l),stderr=subprocess.STDOUT,shell=True)
  print (out)

if __name__ == "__main__":
  getTimes(sys.argv[1])