N = 6
'''
Output: 
* * *
* * *
* * *
'''

##using single loop
print("using single")

for i in range(1,N+1):
    print('*'*N)


## using nested loop

print("using nested")
for i in range(1, N+1):
    for j in range(1, N+1):
        print('*', end ="")
    print()

''' 2) Pattern-2: Right-Angled Triangle Pattern

Input Format: N = 6
Result:
* 
* * 
* * *
* * * *
* * * * *
* * * * * *
'''

##using single loop

print("using single")

for i in range(1,N+1):
    print('*'*i)


## using nested loop

print("using nested")
for i in range(1, N+1):
    for j in range(i):
        print('*', end ="")
    print()

'''
3) Pattern - 3: Right-Angled Number Pyramid
Input Format: N = 6
Result:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
'''


## using nested loop

print("using nested")

for i in range(1, N+1):
    for j in range(1,i+1):
        print(j, end ="")
    print()


''' 4: Right-Angled Number Pyramid - II
Input Format: N = 6
Result:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
'''

##using single loop

print("using single")

for i in range(1,N+1):
    print(str(i)*i)


## using nested loop

print("using nested")
for i in range(1, N+1):
    for j in range(i):
        print(i, end ="")
    print()

'''
5: Inverted Right Pyramid
N = 6
Result:
* * * * * *
* * * * * 
* * * * 
* * * 
* * 
* 
'''

##using single loop

print("using single")

for i in range(N+1, 0,-1):
    print('*'*i)


## using nested loop

print("using nested")
for i in range(1, N+1):
    for j in range(i,N+1):
        print('*', end ="")
    print()


print("using another way in nested")
for i in range(N, 0,-1):
    for j in range(i):
        print('*', end ="")
    print()

'''
6: Inverted Numbered Right Pyramid
Input Format: N = 6
Result:
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1
'''

## using nested loop

print("using nested")

for i in range(N, 0,-1):
    for j in range(1,i+1):
        print(j, end ="")
    print()


'''
7: Star Pyramid
Input Format: N = 6
Result:
     *     
    ***    
   *****   
  *******  
 ********* 
***********
'''

#using single loop

print("using single")

for i in range(1,N+1):
    star  = '*' * (2*i-1)
    space = ' ' * (N-i)
    print(space+star+space)


## using nested loop
for i in range(1,N+1):
    # print space
    for j in range(N-i):
        print(" ", end = "")
    #print()
    # print Star
    for k in range(2*i-1):
        print('*', end = "")
    #print()
    # print Space
    for l in range(N-i):
        print(" ", end = "")
    print()

'''
8: Inverted Star Pyramid
Input Format: N = 6
Result:     
***********
 *********
  *******
   ***** 
    ***    
     *
'''

#using single loop

print("using single")

for i in range(N,0,-1):
    star  = '*' * (2*i-1)
    space = ' ' * (N-i)
    print(space+star+space)


## using nested loop
for i in range(N,0,-1):
    # print space
    for j in range(N-i):
        print(" ", end = "")
    #print()
    # print Star
    for k in range(2*i-1):
        print('*', end = "")
    #print()
    # print Space
    for l in range(N-i):
        print(" ", end = "")
    print()


'''9: Diamond Star Pattern
Input Format: N = 6
Result:   
     *
    ***
   ***** 
  *******
 *********
***********  
***********
 *********
  *******
   ***** 
    ***    
     *
'''
print("Diamond Star Pattern")

#using single loop
for i in range(1,N+1):
    star  = '*' * (2*i-1)
    space = ' ' * (N-i)
    print(space+star+space)

for i in range(N,0,-1):
    star  = '*' * (2*i-1)
    space = ' ' * (N-i)
    print(space+star+space)


for i in range(1,N+1):
    # print space
    for j in range(N-i):
        print(" ", end = "")
    #print()
    # print Star
    for k in range(2*i-1):
        print('*', end = "")
    #print()
    # print Space
    for l in range(N-i):
        print(" ", end = "")
    print()

for i in range(N,0,-1):
    # print space
    for j in range(N-i):
        print(" ", end = "")
    #print()
    # print Star
    for k in range(2*i-1):
        print('*', end = "")
    #print()
    # print Space
    for l in range(N-i):
        print(" ", end = "")
    print()

'''
10: Half Diamond Star Pattern
Input Format: N = 6
Result:   
     *
     **
     *** 
     ****
     *****
     ******  
     *****
     ****
     ***    
     **
     *
'''
print("pattern 10")
#using two loop
for i in range(1,N+1):
    print('*'*i)
for j in range(N-1,0,-1):
    print('*'*j)


#using single loop

rows = 2*N-1
for i in range(1,rows+1):
    if i<=N:
        print('*'*i)
    else:
        print('*'*(2*N-i))

#using nested loop

rows = 2*N-1
for i in range(1,rows+1):
    stars = i
    if i>N:
        stars = 2*N-i
    for j in range(1, stars+1):
        print("*", end = "")
    print()

'''
11: Binary Number Triangle Pattern
Input Format: N = 6
Result:   
1
01
101
0101
10101
010101
'''

#using nested loop

for i in range(1, N+1):
    for j in range(1, i+1):
        if (i+j)%2==0:
            print('1', end ="")
        else:
            print('0', end = "")
    print()
    

'''
12: Number Crown Pattern
Input Format: N = 6
Result:   
1          1
12        21
12       321
1234    4321
12345  54321
123456654321
'''

#using nested loop
for i in range(1, N+1):
    for j in range(1, i+1):
        print(j, end ="")
    space = (2*N) - (2*i)
    print(" " * space, end ="")
    
    for k in range(i,0,-1):
        print(k, end ="")
    print()

'''
13: Increasing Number Triangle Pattern
Input Format: N = 6
Result:   
1
2  3
4  5  6
7  8  9  10
11  12  13  14  15
16  17  18  19  20  21
'''

num =1 
for i in range(1,N+1):
    for j in range(1,i+1):
        print(num,end =" ")
        num+=1
    print()

'''
14: Increasing Letter Triangle Pattern
Input Format: N = 6
Result:   
A
A B
A B C
A B C D
A B C D E
A B C D E F
'''
for i in range(1, N+1):
    num ='A'
    for j in range(1, i+1):
        print(num, end =" ")
        num = chr(ord(num)+1)
    print()

'''
15: Reverse Letter Triangle Pattern
Input Format: N = 6
Result:   
A B C D E F
A B C D E 
A B C D
A B C
A B
A
'''

for i in range(N,0,-1):
    num ='A'
    for j in range(1, i+1):
        print(num, end =" ")
        num = chr(ord(num)+1)
    print()

'''
16: Alpha-Ramp Pattern
Input Format: N = 6
Result:   
A 
B B
C C C
D D D D
E E E E E
F F F F F F
'''
num ='A'
for i in range(N+1):
    for j in range(i+1):
        print(num, end =" ")
    print()
    num = chr(ord(num)+1)
    
'''17: Alpha-Hill Pattern
Input Format: N = 6
Result:   
     A     
    ABA    
   ABCBA   
  ABCDCBA  
 ABCDEDCBA 
ABCDEFEDCBA
'''
for i in range(1,N+1):
    ## print space
    print(" " * (N-i), end ="")
    ##print char
    num = 'A'
    stars = 2*i-1
    breakpoint = (2*i-1)//2
    
    for j in range(1, stars+1):
        print(num, end ="")
        
        if j<= breakpoint:
            num = chr(ord(num)+1)
            
        else:
            num = chr(ord(num)-1)
            
    ## print space
    print("  " * (N-i), end ="")
    print() 

''' 18: Alpha-Triangle Pattern
Input Format: N = 6
Result:   
F
E F
D E F
C D E F
B C D E F
A B C D E F
'''

for i in range(N):
    num = ord('F')
    for j in range(num-i, num+1,1):
        print(chr(j),end =" ")
    print()

'''19: Symmetric-Void Pattern
Input Format: N = 6
Result:   
************
*****  *****
****    ****
***      ***
**        **
*          *
*          *
**        **
***      ***
****    ****
*****  *****
************
'''
#first half    
space = 0
for i in range(N):
    stars = N-i
    #print stars
    for j in range(stars):
        print("*",end ="")
      
    print(" " * space,end ="") 
        #print stars
    for k in range(stars):
        print("*", end ="")
        
    print()  
    space+=2

#second half    
space = 2*N-2  
for i in range(N):
        #print stars
    for k in range(i+1):
        print("*",end ="")
    #print space  
    print(" " * space,end ="") 
        #print stars
    for l in range(i+1):
        print("*", end ="")
        
    print()  
    space-=2

'''20: Symmetric-Butterfly Pattern
Input Format: N = 3
Result: 
*    *
**  **
******
**  **
*    *
'''

space = 2*N-2
rows = 2*N-1
for i in range(1, rows+1):
    stars =i
    if i>N:
        stars =2*N-i
    ## Print Stars
    for j in range(1, stars+1):
        print("*", end = "")
    ##print space 
    for k in range(1, space+1):
        print(" ", end = "")
    ## print stars
    for l in range(1, stars+1):
        print("*", end = "")
    print() ##next line
    if i<N:
        space-=2
    else:
        space+=2

''' 21: Hollow Rectangle Pattern
Input Format: N = 6
Result:   
******
*    *
*    *
*    *
*    *
******
'''

for i in range(N):
    for j in range(N):
        if i == 0 or j == 0 or i == N - 1 or j == N - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

'''
22: The Number Pattern
Input Format: N = 3
Result: 
3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3
'''
for i in range(2*N-1):
    for j in range(2*N-1):
        top = i
        left = j
        right = (2*N-2)-j
        bottom = (2*N-2)-i
        
        print(N- min(min(top,bottom), min(left,right)),end =" ")
    print()
