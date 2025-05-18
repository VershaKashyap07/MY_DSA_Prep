s = "level"
pref = []
suf = []

res = 0
for i in range(1, len(s)):  # Note: up to len(s) - 1 to avoid full string
    pref.append(s[:i])
    suf.append(s[-i:])  # cleaner and same as s[len(s)-i:]

for i in range(len(pref)):
    if pref[i] == suf[i]:
        res = max(res, len(pref[i]))

# Print the longest matching prefix-suffix
for i in pref:
    if len(i) == res:
        print(i)
        break  # only one possible by length


#Optimal:

def longest_prefix_suffix(s):
    n = len(s)
    lps = [0] * n  # LPS array
    length = 0  # length of previous longest prefix-suffix

    i = 1
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  
            else:
                lps[i] = 0
                i += 1

    # lps[n-1] is the length of the longest proper prefix which is also suffix
    return s[:lps[-1]] if lps[-1] > 0 else ""
print(longest_prefix_suffix(s))

