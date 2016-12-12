#1

# this works but it would likely cause a stack overflow error for n > 100
# time complexity: O(2^n)
# space complexity: O(n)

def product_1_to_n(n):  # recursive top --> down
    return n * product_1_to_n(n-1) if n > 1 else 1



#2

# time complexity: O(n)
# space complexity: O(1)

def product_1_to_n(n):  # for loop bottom --> up
    product = 1      
    for i in range(1, n+1): # we assume n >= 1
        product *= i
    return product
