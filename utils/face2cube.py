#!/usr/bin/env python
import sys

#
# converts a face description to a standard cube description
#  input:  FFFFFFFFF RRRRRRRRR BBBBBBBBB LLLLLLLLL UUUUUUUUU DDDDDDDDD
#  output: UF UR UB UL DF DR DB DL FR FL BR BL UFR URB UBL ULF DRF DFL DLB DBR
#
#  input may use any six unique characters, for example, the first letter of
#  the colors on your cube. Each face is scanned from top-left to bottom-right
#

#            UF       UR       UB       UL
CUBIES  = [ [43, 1], [41,10], [37,19], [39,28],
#            DF       DR       DB       DL
            [46, 7], [50,16], [52,25], [48,34], 
#            FR       FL       BR       BL
            [ 5,12], [ 3,32], [21,14], [23,30],
#            UFR         URB         UBL         ULF 
            [44, 2, 9], [38,11,18], [36,20,27], [42,29, 0],
#            DRF         DFL         DLB         DBR
            [47,15, 8], [45, 6,35], [51,33,26], [53,24,17] ]

#           F   R   B   L   U   D
CENTERS = [  4, 13, 22, 31, 40, 49 ]

NOTATION = 'FRBLUD'


#
# main
#


# parse command line
desc = ''.join(sys.argv[1:])
if len(desc) != 6*9:
    print "Invalid input"
    sys.exit (-1)

# create notation conversion map
ncm = {}
for i,c in enumerate(CENTERS):
    ncm[desc[c]] = NOTATION[i]

# produce cube
state = []
for cubie in CUBIES:
    s = ''
    for e in cubie:
        s += ncm[desc[e]]
    state.append (s)

# emit result
print ' '.join(state)
