''' Same implementation as fibonnaci.py with the 'sys.argv' option to run it from the command line.''' 

import sys

argLst = sys.argv


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
    
#print(fib(10))
#print(argLst[0])

print(fib(int(argLst[1])))

#if __name__ = '__main__':
#    Main()
