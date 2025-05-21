'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
'''

#Brute

nums = [1,2,3,1]
k = 3

def check(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                if abs(i-j)<=k:
                   return True 
                    
                    
    return False
    
print(check(nums, k))

#optimal
def check_sliding(nums, k):
    i =0 
    j =0
    st = set()
    
    while j<len(nums):
        if abs(i-j)>k:
            st.remove(nums[i])
            i+=1
        if nums[j] in st:
            return True
        
        st.add(nums[j])
        j+=1
                    
    return False
    
print(check_sliding(nums, k))