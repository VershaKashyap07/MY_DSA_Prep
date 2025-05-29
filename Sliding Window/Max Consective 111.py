nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3


def max_consective_brute(nums,k):
    maxlen = 0
    count = 0
    for i in range(len(nums)):
        count =0
        for j in range(i,len(nums)):
            if nums[j] ==0:
                count +=1

            if count>k:
                break
                
            maxlen = max(maxlen,j-i+1)
                

    return maxlen       
def max_consective_optimal(nums,k):
    cnt_zero = 0
    maxlen  = 0
    i =0
    j =0
    while j < len(nums):
        if nums[j]==0:
            cnt_zero+=1

        while cnt_zero>k:
            if nums[i]==0:
                cnt_zero-=1
            i+=1

        maxlen =  max(maxlen,j-i+1)

        j+=1

    return maxlen

print(max_consective_optimal(nums,k))
print(max_consective_brute(nums,k))