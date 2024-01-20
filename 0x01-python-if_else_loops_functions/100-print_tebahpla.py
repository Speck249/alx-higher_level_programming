#!/usr/bin/python3

for idx in reversed(range(97, 123)):
    print('{}'.format(chr(idx - 32) if idx % 2 != 0 else chr(idx)), end='')
