import subprocess
import sys


def get_time(l):
    out = subprocess.check_output('python3 genPrime.py ' + str(l), stderr=subprocess.STDOUT, shell=True)
    return out


if __name__ == "__main__":

    t = []

    for i in range(int(sys.argv[2])):
        t.append(get_time(sys.argv[1]))

    print(t)
