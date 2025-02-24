#!/usr/bin/env python
import sys
import re

while len(sys.argv) < 4:
    sys.argv.append('0')

dx = float(sys.argv[1])
dy = float(sys.argv[2])
dz = float(sys.argv[3])

def v2str(v):
    v = "%.6f" % v
    return v.rstrip('0').rstrip('.')

def shift_val(s, n, d):
    p = s.find(n)
    if p >= 0:
        out = s[:p + 1]
        m = re.search("[+-]?[0-9.]+", s[p + 1:])
        v = float(m.group()) + d
        out += v2str(v) + s[p + 1 + m.end():]
        return out

    else:
        return s

for line in sys.stdin:
    line = shift_val(line, 'X', dx)
    line = shift_val(line, 'Y', dy)
    line = shift_val(line, 'Z', dz)
    sys.stdout.write(line)
