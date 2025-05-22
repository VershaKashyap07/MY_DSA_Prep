nums = [1,3,5,2,7,5]
minK = 1
maxK = 5
n = len(nums)

def subarray_Brute(nums, minK, maxK, n):
    ans = 0
    for i in range(n):
        curr_min = float('inf')
        curr_max = float('-inf')
        for j in range(i,n):
            curr_min =  min(curr_min, nums[j])
            curr_max = max(curr_max, nums[j])
            if curr_min== minK and curr_max == maxK:
                ans+=1

    return ans

print(subarray_Brute(nums, minK, maxK, n))

##optimal

def subarray_Optimal(nums, minK, maxK, n):
    minPos = -1
    maxPos = -1
    culpritIndex = -1
    smaller  = 0
    ans = 0
    for i in range(n):
        if nums[i] < minK or nums[i] >maxK:
            culpritIndex = i

        if nums[i] == minK:
            minPos =i 

        if nums[i] == maxK:
            maxPos =i 
        smaller =  min(minPos, maxPos)

        ans += max(0,  smaller - culpritIndex)

    return ans

print(subarray_Optimal(nums, minK, maxK, n))