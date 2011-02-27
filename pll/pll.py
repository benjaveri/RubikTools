#!/usr/bin/env python
import sys
sys.path.append ("../utils")
from solver import solve
import subprocess

CASES = [
#   [ 'UBL','UB','URB','UR','UFR','UF','ULF','UL' ],
    [ 'UBL','UR','URB','UL','UFR','UF','ULF','UB' ],
    [ 'UBL','UL','URB','UB','UFR','UF','ULF','UR' ],
]

CUBE = [ 'UF','UR','UB','UL','DF','DR','DB','DL','FR','FL','BR','BL','UFR','URB','UBL','ULF','DRF','DFL','DLB','DBR' ]
IDX  = [ 14, 2, 13, 1, 12, 0, 15, 3 ]

for case in CASES:
    desc = CUBE[:]
    for i,c in enumerate(case):
        desc[IDX[i]] = c
    print desc
    for sol in solve(desc):
        print sol
        
        
    