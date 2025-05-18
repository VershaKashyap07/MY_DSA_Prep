s = "((("

#brute Force
def Valid_Parenthesis(s):
    open =0
    stack = []
    for i in s:
        if i =='(':
            stack.append(i)
        elif i ==')':
            if stack:
                stack.pop()
            else:
                open +=1

    return len(stack)+ open

print(Valid_Parenthesis(s))
    
#without Stack

def valid_paren(str):
    open = 0
    size = 0
    for i in str:
        if i == "(":
            size+=1
        elif i ==')':
            if size==0:
                open+=1
            else:
                size-=1
    
    return open+size

print(valid_paren(str))
