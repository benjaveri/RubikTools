#!/usr/bin/env python
import sys
import pickle
sys.path.append ("../utils")
from solver import solve
import subprocess

# permutations
CASES = [
    [ 0,3,2, 5,4,1, 6,7,8 ],
    [ 0,5,2, 1,4,3, 6,7,8 ],
    [ 2,1,8, 3,4,5, 6,7,0 ],
    [ 8,1,0, 3,4,5, 6,7,2 ],
    [ 0,3,2, 1,4,7, 6,5,8 ],
    [ 0,7,2, 5,4,3, 6,1,8 ],
    [ 6,1,8, 3,4,5, 0,7,2 ],
    [ 0,1,8, 5,4,3, 6,7,2 ],
    [ 8,5,2, 3,4,1, 6,7,0 ],
    [ 0,7,8, 3,4,5, 6,1,2 ],
    [ 2,1,0, 3,4,7, 6,5,8 ],
    [ 0,5,2, 3,4,1, 8,7,6 ],
    [ 0,1,8, 3,4,7, 6,5,2 ],
    [ 0,5,8, 3,4,1, 6,7,2 ],
    [ 8,3,2, 1,4,5, 6,7,0 ],
    [ 6,7,0, 1,4,5, 2,3,8 ],
    [ 6,5,0, 1,4,3, 2,7,8 ],
    [ 8,1,2, 7,4,3, 0,5,6 ],
    [ 8,3,2, 7,4,5, 0,1,6 ],
    [ 8,1,2, 5,4,3, 6,7,0 ],
    [ 0,1,6, 5,4,3, 2,7,8 ],
]

# rotate cases so i like them
ROT  = [ 0,0,1,1, 1,0,1,1, 0,1,2,0, 1,1,0,2, 2,3,3,0, 0 ]
TROT = [ 6,3,0, 7,4,1, 8,5,2 ]
for i,case in enumerate(CASES[:]):
    for j in range(ROT[i]):
        case = [ case[k] for k in TROT ]
        case = [ TROT.index(case[k]) for k in range(9) ]
    CASES[i] = case
# reorder so i like em more
CASES = [ CASES[i] for i in [ 0,1,2,3, 10,11,12,13, 15,16,17,18, 6,9,4,8, 5,7,19,20, 14 ]]

# cubie data
CUBE = [ 'UF','UR','UB','UL','DF','DR','DB','DL','FR','FL','BR','BL','UFR','URB','UBL','ULF','DRF','DFL','DLB','DBR' ]
TLAY = [ 'UBL', 'UB', 'URB', 'UL', 'xx', 'UR', 'ULF', 'UF', 'UFR' ]
TIDX = [ ((['xx'] + CUBE).index(i)-1) for i in TLAY ]

#
# create set of problems
#
probs = []
for case in CASES:
    # cases are given in 'solved' space, convert to problem space
    a = [ (case[i],i) for i in range(9) ]
    a.sort()
    # make problem
    prob = CUBE[:]
    for i,j in a:
        if TIDX[j] >= 0:
            prob[TIDX[j]] = TLAY[i]
    # save
    probs.append (prob)

#
# solve problems
#
sols = solve(probs)
    
#
# save results
#
with open('data.bin','wb') as f:
    pickle.dump (f,CASES)
    pickle.dump (f,probs)
    pickle.dump (f,sols)

