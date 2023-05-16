#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv)
    result = 0
    for i in range(n - 1):
        result += int(sys.argv[i + 1])
    print(result)
