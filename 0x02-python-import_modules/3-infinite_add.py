#!/usr/bin/python3
import sys

def main():
    answer = 0
    
    for arg in sys.argv[1:]:
        answer += int(arg)
    print(answer)

if __name__ == '__main__':
    main()
