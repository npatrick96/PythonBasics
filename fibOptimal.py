def fibSlow(n):
    if n <= 1:
        return n 
    else:
        return fibSlow(n-1) + fibSlow(n-1)

def fibFast1(n):
    fibs = [0] * (n+1) # 0th to the nth elt
    fibs[1] = 1 # fibs[0] = 0 is already set
    for i in range(2, n+1):
        fibs[i] = fibs[i-1] + fibs[i-2]
    return fibs[i]
        
#print (fibSlow(30)) # this is very slow
print (fibFast1(40)) # way faster !!!
    
    