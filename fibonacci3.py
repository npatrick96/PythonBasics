''' Same implementation as fibonnaci.py with the 'argparse' option to run it from the command line.

Docs: https://docs.python.org/3/library/argparse.html + https://www.youtube.com/watch?v=rnatu3xxVQE
''' 



import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
    

parser = argparse.ArgumentParser()
parser.add_argument('num', help = 'nth fib number', type=int)
args = parser.parse_args()
print(fib(args.num))


# import argparse
# 
# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a+b
#     return a
#     
# def Main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('num', help = 'nth fib number', type=int)
#     args = parser.parse_args()
#     print(fib(args.num))
# 
# if __name__ == '__main__':
#     Main()
    

