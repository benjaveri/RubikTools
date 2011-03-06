#!/usr/bin/env python
import sys
sys.path.append ("../utils")
from solver import solve
import subprocess
import math

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
#for sol in solve(probs):
#    print sol
            
#
# create svg images for each problem
#
def line(f,x0,y0,x1,y1):
    f.write ('<line stroke="black" x1="%f" y1="%f" x2="%f" y2="%f" stroke-width="1" />\n' % (x0,y0,x1,y1))

def rect(f,x,y,w,h):
    f.write ('<rect stroke="black" fill="white" x="%d" y="%d" width="%d" height="%d" stroke-width="1" />\n' % (x,y,w,h))

def arrow(f,a,b):
    x0 = (a % 3)*10 + 5
    y0 = (a / 3)*10 + 5
    x1 = (b % 3)*10 + 5
    y1 = (b / 3)*10 + 5
    dx = x1-x0
    dy = y1-y0
    ln = math.sqrt(1.0*dx*dx+dy*dy)
    dx /= ln
    dy /= ln
    
    a = (x0+3*dx,y0+3*dy)
    b = (x1-3*dx,y1-3*dy)
    z = (b[0]-3*dx,b[1]-3*dy)
    c = (z[0]-1*dy,z[1]+1*dx)
    d = (z[0]+1*dy,z[1]-1*dx)
    
    line (f,a[0],a[1],b[0],b[1])
    line (f,c[0],c[1],b[0],b[1])
    line (f,d[0],d[1],b[0],b[1])
    
    
for i,case in enumerate(CASES):
    with open("html/pll%02d.svg" % i,"w") as f:
        f.write ('<?xml version="1.0" encoding="iso-8859-1" standalone="no"?>\n')
        f.write ('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.0//EN" "http://www.w3.org/TR/SVG/DTD/svg10.dtd">\n')
        f.write ('<svg viewBox="0 0 30 30" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n')
        f.write ('<g id="mainlayer">\n')
        for x in range(3):
            for y in range(3):
                rect (f,x*10,y*10,10,10)
        for i,c in enumerate(case):
            if i != c: arrow (f,i,c)
        f.write ('</g>\n');
        f.write ('</svg>\n')
                    
with open("html/index.html","w") as f:
    f.write ('<html><body><table>\n')
    for y in range(6):
        f.write ('<tr>')
        for x in range(4):
            i = y*4+x
            f.write ('<td>')
            if i < len(CASES):
                f.write ("<embed width='100' height='100' src='pll%02d.svg' type='image/svg+xml' />" % i)
                f.write ('%02d' % i)
            f.write ('</td>')
        f.write ('</tr>\n')
    f.write ('</table></body></html>\n')
    