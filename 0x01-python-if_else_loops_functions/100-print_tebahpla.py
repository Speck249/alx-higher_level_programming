#!/usr/bin/python3

for i in reversed(range(97, 123)):
    if i % 2 == 0:
        j = 0
    else:
        j = 32
    print("{:c}".format(i - j), end="")
