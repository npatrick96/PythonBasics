# given two words, find if second word is the round rotation of first word

def roundRot(w1, w2): 
    if len(w1) < 1 or len(w2) < 1:
        return False
    elif len(w1) != len(w2):
        #print
        return False
    else:
        sort1, sort2 = sorted(w1), sorted(w2)
        for i in range(len(sort1)):
            if sort1[i] != sort2[i]:
                return False
        return True
        
print(roundRot("abc", "cab"))
print(roundRot("aa", "ab"))
print(roundRot("abcdabza", "cdabzaab"))

# tested using Atom Script Package