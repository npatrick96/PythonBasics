str1 = "hellolle"
str2 = "wowpurerocks"
    

def getSubs(st):
    n = len(st)
    return [st[i:j+1] for i in xrange(n) for j in xrange(i, n)]
print(getSubs("123"))



def isPali(st):
    n = len(st)
    for i in range(n):
        if st[i] != st[n-1-i]:
            return False
    return True
print(isPali("1"))

def count_palindromes(s):
    s_subs = getSubs(s)
    ct = 0
    for i in s_subs:
        if isPali(i):
            ct = ct + 1
    print(ct)
    return(ct)

count_palindromes(str1)
count_palindromes(str2)
        