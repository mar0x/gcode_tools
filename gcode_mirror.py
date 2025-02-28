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

def mirror_arc(s):
    p = s.find('G')
    if p >= 0:
        out = s[:p + 1]
        m = re.search("[+-]?[0-9.]+", s[p + 1:])
        v = m.group()
        try:
            if v == '2':
                v = '3'
            else:
                if v == '3':
                    v = '2'
        except:
            pass
        out += v + s[p + 1 + m.end():]
        return out

    else:
        return s

while len(sys.argv) < 2:
    sys.argv.append('Y')

for line in sys.stdin:
    if line.startswith('G'):
        line = mirror_arc(line)
        if sys.argv[1] == 'Y':
            line = mirror_val(line, 'X')
            line = mirror_val(line, 'I')
        else:
            line = mirror_val(line, 'Y')
            line = mirror_val(line, 'J')
    sys.stdout.write(line)
