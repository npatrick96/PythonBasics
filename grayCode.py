''' Given two hexadecimal numbers find if they can be consecutive in gray code 

- gray code: https://en.wikipedia.org/wiki/Gray_code
- consecutive gray code numbers should only differ in one bit
- solution based on: http://stackoverflow.com/a/35690973/6476668
'''

def consecutive(a, b):
    strA, strB = str(a), str(b)
    if len(strA) < 1 or len(strA) < 1:
        return False
    elif len(strA) != len(strB):
        return False
    count = 0
    for i in range(len(strA)):
        if strA[i] != strB[i]:
            count += 1
    #print(count)
    if count == 1:
        return True
    else:
        return False
        
# For example, 10001000, 10001001 should return true
print(consecutive(10001000, 10001001))
print(consecutive(10001001, 10001000))        

# 10001000, 10011001 are not successive in gray code     
print(consecutive(10001000, 10011001))
print(consecutive(10011001, 10001000))

