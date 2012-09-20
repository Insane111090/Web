import sys
year=sys.argv[1]
while 1:
year = int(year)
if year % 400 ==0:
print u'Vysokosniy'
break
elif year % 100 ==0:
print u'Ne vysokosniy'
break
elif year % 4 ==0:
print u'Vysokosniy'
break
else:
print u'ne visokosniy'
break