#!/usr/bin/env python
import sys
import re

while len(sys.argv) < 4:
    sys.argv.append('1')

sx = float(sys.argv[1])
sy = float(sys.argv[2])
sz = float(sys.argv[3])

def scale_val(s, n, d):
    p = s.find(n)
    if p >= 0:
        out = s[:p + 1]
        m = re.search("[+-]?[0-9.]+", s[p + 1:])
        v = m.group()
        try:
            v = float(m.group()) * d
        except:
            pass
        out += str(v) + s[p + 1 + m.end():]
        return out

    else:
        return s

for line in sys.stdin:
    if line.startswith('G'):
        line = scale_val(line, 'X', sx)
        line = scale_val(line, 'I', sx)
        line = scale_val(line, 'Y', sy)
        line = scale_val(line, 'J', sy)
        # line = scale_val(line, 'Z', sz)
    sys.stdout.write(line)
