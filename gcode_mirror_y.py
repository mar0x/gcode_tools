#!/usr/bin/env python
import sys
import re

def mirror_val(s, n):
    p = s.find(n)
    if p >= 0:
        out = s[:p + 1]
        m = re.search("[+-]?[0-9.]+", s[p + 1:])
        v = m.group()
        try:
            f = float(v)
            if v.startswith('-'):
                v = v[1:]
            else:
                v = '-' + v
        except:
            pass
        out += v + s[p + 1 + m.end():]
        return out

    else:
        return s

for line in sys.stdin:
    if line.startswith('G'):
        line = mirror_val(line, 'X')
        line = mirror_val(line, 'I')
        #line = scale_val(line, 'Y', sy)
        #line = scale_val(line, 'J', sy)
        # line = scale_val(line, 'Z', sz)
    sys.stdout.write(line)
