s = "ADOBECODEBANC"
t = "ABC"
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
    print("")
else:
    print(s[start_i: start_i + window])
