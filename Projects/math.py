import sys
import math
print "Enter what you whant to see in format <name> : <accuracy>:"
name=sys.argv[1]
tochn=sys.argv[3]
tochn = int(tochn)
if name =='pi':
    print round(math.pi,tochn)
if name == 'e':
    print round(math.e,tochn)
