#!/usr/bin/env python
import sys
import re

while len(sys.argv) < 4:
    sys.argv.append('0')

zstep = float(sys.argv[1])
zcount = int(sys.argv[2])

def v2str(v):
    v = "%.6f" % v
    return v.rstrip('0').rstrip('.')

def shift_val(s, n, d):
    if 'G00' in s:
        return s

    p = s.find(n)
    if p >= 0:
        out = s[:p + 1]
        m = re.search("[+-]?[0-9.]+", s[p + 1:])
        v = float(m.group()) + d
        out += v2str(v) + s[p + 1 + m.end():]
        return out

    else:
        return s

lines = []

for line in sys.stdin:
    lines.append(line)
    sys.stdout.write(line)

for n in range(1, zcount + 1):
    dz = n * zstep
    for line in lines:
        line = shift_val(line, 'Z', dz)
        sys.stdout.write(line)
