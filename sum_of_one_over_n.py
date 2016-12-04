# The sum of 1/n is a harmonic series. Below is a simple function that can be used to calculate it.
# Source:  https://en.wikipedia.org/wiki/Harmonic_series_(mathematics)

def sum(n):
    sum = 0
    for i in range (1, n+1):
        sum = sum + 1/i
    print (sum)
    #return sum
        
