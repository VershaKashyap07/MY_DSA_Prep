s = "ADOBECODEBANC"
t = "ABC"

def check_substring(s,t,i,j):
    t_map = {}
    s_map = {}

    for k in s[i:j+1]:
        s_map[k] = s_map.get(k,0)+1

    for l in t:
        t_map[l] = t_map.get(l,0)+1

    for key, val in t_map.items():
        if s_map.get(key,0)< val:
            return False
        
    return True

def minimum_substring_brute(s,t): 
    length = float('inf')
    start_i = -1
    for i in range(len(s)):
        for j in range(i,len(s)):
            if check_substring(s,t,i,j):
                if j-i+1< length:
                    length =  j-i+1
                    start_i = i
                    # we want minimum window
                break 

    if length == float('inf'):
        return ""
    else:
        return s[start_i: start_i + length]

print(minimum_substring_brute(s,t))

def minimum_substring_optimal(s,t):
    t_mpp = {}
    for i in t:
        t_mpp[i] = t_mpp.get(i, 0) + 1

    i = 0
    j = 0
    cntreq = len(t)
    window = float('inf')
    start_i = 0

    while j < len(s):
        if t_mpp.get(s[j], 0) > 0:
            cntreq -= 1

        t_mpp[s[j]] = t_mpp.get(s[j], 0) - 1

        while cntreq == 0:
            if j - i + 1 < window:
                window = j - i + 1
                start_i = i

            t_mpp[s[i]] = t_mpp.get(s[i], 0) + 1

            if t_mpp.get(s[i], 0) > 0:
                cntreq += 1
            i += 1

        j += 1

    if window == float('inf'):
        return ""
    else:
        return s[start_i: start_i + window]
print(minimum_substring_optimal(s,t))