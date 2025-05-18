txt = "sadbutsad"
pattern = "sad"
n = len(txt)
m = len(pattern)
res = []
for i in range(n-m+1):
    match = True
    for j in range(m):
        if txt[i+j]!= pattern[j]:
            match = False
            break
    if match:
        res.append(i)
        
print(res)

##using KMP


def find_LPS(pattern):
    LPS = [0] *len(pattern)
    length = 0
    for i in range(1,len(pattern)):
        if pattern[i] == pattern[length]:
            length+=1
            LPS[i] = length
        else:
            if length!= 0:
                length = LPS[length-1]
                if pattern[i] == pattern[length]:
                    length+=1
                    LPS[i] = length
            else:
                LPS[i] = 0
    return LPS
    
print(find_LPS(pattern))


def KMP(txt,pattern):
    i =0
    j =0
    m = len(pattern)
    n  = len(txt)
    res = []
    LPS = find_LPS(pattern)
    while i<n:
        if txt[i] == pattern[j]:
            i+=1
            j+=1
        if j==m:
            res.append(i-j+1) ##! based indexing in case of 0 return i-j
            j =  LPS[j-1]
        elif txt[i] != pattern[j]:
            if j!=0:
                j = LPS[j-1]
            else:
                i+=1
            
    return res
     
print(KMP(txt,pattern)) 