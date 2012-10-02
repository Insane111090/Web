# -*- encoding: utf-8 -*-
import sys
while 1:
    try:
        year = sys.argv[1]
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
    except(ValueError):
        print "Please enter a number"
        break
    except Exception, err:
        print "Unexpected error:", err
        break
