#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

def main():
    if len(sys.argv) <= 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        x = int(sys.argv[1])
        y = sys.argv[2]
        z = int(sys.argv[3])

        if y == '+':
            print('{} {} {} = {}'.format(x, y, z, add(x, z)))
        elif y == '-':
            print('{} {} {} = {}'.format(x, y, z, sub(x, z)))
        elif y == '*':
            print('{} {} {} = {}'.format(x, y, z, mul(x, z)))
        elif y == '/':
            print('{} {} {} = {}'.format(x, y, z, div(x, z)))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            sys.exit(1)

if __name__ == '__main__':
    main()
