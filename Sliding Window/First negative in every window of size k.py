from collections import deque
arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3

def First_Neg(arr,k):
    res = []
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if j-i+1 == k:
                flag = 0
                for l in range(i,j+1):
                    if arr[l]<0:
                        flag = 1
                        res.append(arr[l])
                        break
                if flag ==0:
                    res.append(0)
                break  
                
    return res
            
print(First_Neg(arr,k))

##better

def First_Neg_better(arr,k):
    res = []
    for i in range(len(arr)-k+1):
        flag = False
        for j in range(i,i+k):
            if arr[j]<0:
                flag = True
                res.append(arr[j])
                break
            
        if not flag:
            res.append(0)
                 
    return res
            
print(First_Neg_better(arr,k))




def First_Neg_sliding(arr,k):
    res = []
    q = deque()
    i = 0
    
    for j in range(len(arr)):
        if arr[j]<0:
            q.append(j)
            
        if j-i+1 ==k:
            if q:
                res.append(arr[q[0]])
            else:
                res.append(0)
        
            if q and q[0]==i:
                q.popleft()
            i+=1
            
    return res
            
            
print(First_Neg_sliding(arr,k))