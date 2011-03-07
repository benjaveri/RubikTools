import subprocess
import re

def solve (states):
    # prepare input
    lines = [ ' '.join(s) for s in states ]
    input = '\n'.join(lines + [ 'exit\n' ])
    
    # spawn michael's excellent solver
    P = subprocess.Popen(["../solver/clsolve"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,stdin=subprocess.PIPE,shell=False)
    out,err = P.communicate(input)

    #print out
    #with open('out.txt','w') as f:
    #    f.write (out)

    # parse results    
    results = []
    part = []
    for line in out.splitlines(False):
        if line.startswith('INPUT:'):
            results.append (part)
            part.sort()
            part = []
        elif line.startswith('RESULT:'):
            line = line[8:].split(',')
            count = int(line[0])
            seq   = line[1].strip().split()
            part.append ((count,seq))
    
    # done        
    return results[1:]
    