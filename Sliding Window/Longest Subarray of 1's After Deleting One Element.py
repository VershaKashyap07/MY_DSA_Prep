nums = [1,1,0,1]
def longestSubarray(nums):
    i = 0
    cntZero = 0
    maxLen = 0

    for j in range(len(nums)):
        if nums[j] == 0:
            cntZero += 1

        while cntZero > 1:
            if nums[i] == 0:
                cntZero -= 1
            i += 1

        # we always delete 1 element, so window length is (j - i)
        maxLen = max(maxLen, j - i)

    return maxLen

print(longestSubarray(nums))

def longestSubarrayBetter(nums):
    i = 0
    cntZero = 0
    maxLen = 0
    zerolastIndex = -1

    for j in range(len(nums)):
        if nums[j] == 0:
            zerolastIndex = j
            cntZero += 1

        while cntZero > 1:
            if nums[i] == 0:
                cntZero -= 1
            i += 1

        # we always delete 1 element, so window length is (j - i)
        maxLen = max(maxLen, j - i)

    return maxLen

print(longestSubarrayBetter(nums))