# Fibonacci #1: naive recursive algorithm
def fibSlow(n):
    if n <= 1:
        return n 
    else:
        return fibSlow(n-1) + fibSlow(n-1)
#print (fibSlow(30)) # this is very slow        


        
# Fibonacci #2: explicitly filling in a table with a loop
def fibFast1(n):
    fibs = [0] * (n+1) # 0th to the nth elt
    fibs[1] = 1 # fibs[0] = 0 is already set
    for i in range(2, n+1):
        fibs[i] = fibs[i-1] + fibs[i-2]
    return fibs[i]
print (fibFast1(40)) # faster !!!



# Fibonacci #3: recursion with memoization
# Keep a global table to remember the results of fib3
fibtable = [0,1]
def fibFast2(n):
# Expand the table as necessary
    while len(fibtable) < n+1:
        fibtable.append(-1)
# Fill in the table recursively (only if necessary)
    if fibtable[n] == -1:
        fibtable[n] = fibFast2(n-1) + fibFast2(n-2)
    return fibtable[n]
print (fibFast2(40)) # faster !!!
lst = [0] * 10
print(lst)
print(4%2)



def fibFast3(n):
    fibs = [0] * (n+1)
    fibs[1] = 1
    fibs[2] = 1
    for i in range(3, n+1):
        #print (fibs)
        if i%2 == 0:
            fibs[i] = fibs[i/2] * ( fibs[1+(i/2)] + fibs[-1+(i/2)])
        #else:
            #fibs[i] = fibs[i-1] + fibs[i-2]
    return fibs[i]
print (fibFast3(40)) # faster !!!
    
    
    
    