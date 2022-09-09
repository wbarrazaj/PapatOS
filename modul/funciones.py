import os
import sys
import psutil
import time
from datetime import datetime, timedelta


def bytes2human(n, format="%(value).1f%(symbol)s"):
    """Used by various scripts. See:
    http://goo.gl/zeJZl

    >>> bytes2human(10000)
    '9.8K'
    >>> bytes2human(100001221)
    '95.4M'
    """
    symbols = ('B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols[1:]):
        prefix[s] = 1 << (i + 1) * 10
    for symbol in reversed(symbols[1:]):
        if n >= prefix[symbol]:
            value = float(n) / prefix[symbol]
            return format % locals()
    return format % dict(symbol=symbols[0], value=n)


def print_(msg):
    print(msg)


def printlog(prompt):
    year, mon, mday, hour, min, sec, wday, yday, isdst = time.localtime()
    print("%04d-%02d-%02d %02d:%02d:%02d %s" % (year, mon , mday, hour, min, 
sec, prompt))


print_("Hola")

printlog("Error 111")

print(bytes2human(1024*1024*1024*1024*1024))

printlog("Hola")