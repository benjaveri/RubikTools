#!/usr/bin/env python
import sys
import math
import pickle

#
# read results
#
with open('data.bin','rb') as f:
    CASES = pickle.load(f)
    probs = pickle.load(f)
    sols = pickle.load(f)

#
# create svg images for each problem
#
def line(f,x0,y0,x1,y1):
    f.write ('<line stroke="black" x1="%f" y1="%f" x2="%f" y2="%f" stroke-width=".3" />\n' % (x0,y0,x1,y1))

def rect(f,x,y,w,h):
    f.write ('<rect stroke="black" fill="white" x="%d" y="%d" width="%d" height="%d" stroke-width=".1" />\n' % (x,y,w,h))

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
    
    S = 1.0 # distance from cubie center to arrowhead
    B = 2.5 # arrowhead size
    W = 0.7 # arrowhead width
    
    a = (x0+S*dx,y0+S*dy)
    b = (x1-S*dx,y1-S*dy)
    z = (b[0]-B*dx,b[1]-B*dy)
    c = (z[0]-W*dy,z[1]+W*dx)
    d = (z[0]+W*dy,z[1]-W*dx)
    
    line (f,a[0],a[1],b[0],b[1])
    line (f,c[0],c[1],b[0],b[1])
    line (f,d[0],d[1],b[0],b[1])
    
    
for i,case in enumerate(CASES):
    with open("html/pll%02d.svg" % i,"w") as f:
        f.write ('<?xml version="1.0" encoding="iso-8859-1" standalone="no"?>\n')
        f.write ('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.0//EN" "http://www.w3.org/TR/SVG/DTD/svg10.dtd">\n')
        f.write ('<svg viewBox="-3 -3 33 33" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n')
        f.write ('<g id="mainlayer">\n')
        for x in range(3):
            for y in range(3):
                rect (f,x*10,y*10,10,10)
        for i,c in enumerate(case):
            if i != c: arrow (f,c,i)
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
                sol = sols[i]
                if len(sol) > 0: f.write ('%s' % sol[0][1])
            f.write ('</td>')
        f.write ('</tr>\n')
    f.write ('</table></body></html>\n')
    