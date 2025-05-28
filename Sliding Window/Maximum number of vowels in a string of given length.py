s = "leetcode"
k = 3



##brute force

def check_vowelCount(s,i,j):
    cnt = 0
    for char in s[i:j+1]:
        if char == 'a' or char =='e' or  char =='i' or char =='o' or char =='u':
            cnt+=1

    return cnt

def maxVowels_Brute(s,k):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if j-i+1 ==k:
                count = max(count,check_vowelCount(s,i,j))
                break

    return count
            
print(maxVowels_Brute(s,k))

def maxVowels_Optimal(s,k):
    i, j,cnt,maxcnt = 0,0,0,0
    while j< len(s):
        if s[j] == 'a' or s[j] =='e' or  s[j] =='i' or s[j] =='o' or s[j] =='u':
            cnt+=1
        if j-i+1 ==k:
            maxcnt =  max(cnt,maxcnt)
            if s[i] =='a' or s[i] =='e' or  s[i] =='i' or s[i] =='o' or s[i] =='u':
                cnt -=1
            i+=1
        j+=1

    return maxcnt

print(maxVowels_Optimal(s,k))