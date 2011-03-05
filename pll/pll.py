#!/usr/bin/env python
import sys
sys.path.append ("../utils")
from solver import solve
import subprocess

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
    print a
    # make problem
    prob = CUBE[:]
    for i,j in a:
        if TIDX[j] >= 0:
            prob[TIDX[j]] = TLAY[i]
    print prob
    # save
    probs.append (prob)

sols = solve(probs)
print sols
for i,sol in enumerate(sols):
    print probs[i]
    print sol[i]
            
        
    