import sys
import math
name=sys.argv[1]
tochn=sys.argv[2]
tochn = int(tochn)
if name == 'pi':
print round(math.pi,tochn)
if name == 'e':
print round(math.e,tochn)