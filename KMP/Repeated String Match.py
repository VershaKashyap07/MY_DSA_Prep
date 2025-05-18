a = 'a'
b = 'aa'

#Brute Force
def find_substring(a,b):
    repeat_a =""
    count =0
    
    while len(repeat_a)< len(a)+ len(b):
        repeat_a += a
        count+=1
        
        if b in repeat_a:
            return count
            
    return -1
             
print(find_substring(a,b))

##optimal

def computeLPS(pattern):
    lps = [0] * len(pattern)
    length = 0  # length of the previous longest prefix suffix

    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # don't increment i here
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    lps = computeLPS(pattern)
    i = 0  # index for text
    j = 0  # index for pattern

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return True  # match found
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False


def repeatedStringMatch(a, b):
    repeated = ""
    count = 0

    # Repeat until the length is enough to contain b
    while len(repeated) < len(b) + len(a):
        repeated += a
        count += 1
        if kmp_search(repeated, b):
            return count

    return -1
