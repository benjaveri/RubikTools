import subprocess
import re

def solve (state):
    P = subprocess.Popen(["../solver/clsolve"]+state,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,stdin=subprocess.PIPE,shell=False)
    out,err = P.communicate('')
    res = []
    for line in out.splitlines(False):
        if line.startswith('RESULT:'):
            line = line[8:].split(',')
            count = int(line[0])
            seq   = line[1].strip().split()
            res.append ((count,seq))
    res.sort()
    return res
    