s = "abcd"

def palindrome(s):
    rev = ""
    for i in range(len(s)-1,-1,-1):
        rev+= s[i]
       
    for i in range(len(s)):
        if s[: len(s)-i] == rev[i:]:
            return rev[:i] +s
            
    return rev+s    

print(palindrome(s))

#optimal
def palindrome(s):
    rev = s[::-1]
    s1 = s + '-' + rev
    
    LPS = [0] * len(s1)
    length = 0
    i = 1
    
    while i < len(s1):
        if s1[i] == s1[length]:
            length += 1
            LPS[i] = length
            i += 1
        else:
            if length != 0:
                length = LPS[length - 1]
            else:
                LPS[i] = 0  
                i += 1
    
    res = LPS[-1]
    return rev[:len(rev) - res] + s
