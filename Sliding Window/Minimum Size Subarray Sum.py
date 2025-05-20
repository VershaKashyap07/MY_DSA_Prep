arr = [2,3,1,2,4,3]
target =7

def minSubArrayLen(arr,target):
    length = float('inf')
    summ = 0
    for i in range(len(arr)):
        summ = 0
        for j in range(i,len(arr)):
            summ+= arr[j]
            
            if summ >= target:
                length = min(length, j-i+1)
                break
                
    return length if length != float('inf') else 0
            
print(minSubArrayLen(arr,target))

##optimal
arr = [1,1,1,1,1,1,1,1]
target = 11

def minSubArrayLen_slidng(arr,target):
    length = float('inf')
    summ = 0
    i= 0
    for j in range(len(arr)):
        summ+= arr[j]
        while summ >= target:
            length = min(length, j-i+1)
            summ-= arr[i]
            i+=1
                
    return length if length != float('inf') else 0
            
print(minSubArrayLen_slidng(arr,target))