import sys
import math
name=sys.argv[1]
tochn=sys.argv[3]
print "Enter what you whant to see in format <name> : <accuracy>:"
tochn = int(tochn)
if name =='pi':
print round(math.pi,tochn)
if name == 'e':
print round(math.e,tochn)