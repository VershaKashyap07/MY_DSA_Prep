txt = "forxxorfxdofr"
pat = "for"
count = 0

def make_one(s):
    mpp = {}
    for i in range(len(s)):
        mpp[s[i]] =  mpp.get(s[i],0)+1
    return mpp
        
pat_map = make_one(pat)   
    
for i in range(len(txt)-len(pat)+1):
        window =  txt[i:i+len(pat)]
        window_freq = make_one(window)   
        
        if window_freq == pat_map:
            count+=1
            
print(count)

##optimal

txt = "aabaabaa"
pat = "aaba"
count = 0
i = 0  
k = len(pat)
match =0

def make_one(s):
    mpp = {}
    for i in s:
        mpp[i] =  mpp.get(i,0)+1
    return mpp
        
pat_map = make_one(pat)  

for j in range(len(txt)):
    if txt[j] in pat_map:
        pat_map[txt[j]]-=1
        if pat_map[txt[j]] ==0:
            match+=1
        
    if j-i+1>k:
        
        if txt[i] in pat_map:
            if pat_map[txt[i]] ==0:
                match-=1
            pat_map[txt[i]]+=1
        i+=1
        
    if match == len(pat_map):
       count+=1
    
            
print(count)
        