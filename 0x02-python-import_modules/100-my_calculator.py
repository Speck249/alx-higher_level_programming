#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    length = len(sys.argv)
    result = 0

    if (length - 1)  != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = sys.argv[2]

    if operator != '+' and operator != '-' and operator != '*' and operator != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if operator == '+':
        result = add(a, b)
        print("{:d} + {:d} = {:d}".format(a, b, result))

    elif operator == '-':
        result = sub(a, b)
        print("{:d} - {:d} = {:d}".format(a, b, result))

    elif operator == '*':
        result = div(a, b)
        print("{:d} * {:d} = {:d}".format(a, b, result))

    elif operator == '/':
        result = div(a, b)
        print("{:d} / {:d} = {:d}".format(a, b, result))
