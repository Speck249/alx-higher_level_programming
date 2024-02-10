#!/usr/bin/python3
import sys

def main():
    n = len(sys.argv)

    if n == 1:
        print('{} arguments.'.format(n - 1))
    elif n == 2:
        print('{} argument:'.format(n - 1))
        print('{}: {}'.format(n - 1, sys.argv[1]))
    elif n > 2:
        print('{} arguments:'.format(n - 1))

        idx = 1
        while idx < n:
            print('{}: {}'.format(idx, sys.argv[idx]))
            idx += 1

if __name__ == '__main__':
    main()
