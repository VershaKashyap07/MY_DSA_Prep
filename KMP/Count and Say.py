def Count_Say(n):
    if n == 1:
        return '1'
    
    say = Count_Say(n - 1)
    result = ''
    i = 0
    
    while i < len(say):
        count = 1
        while i + 1 < len(say) and say[i] == say[i + 1]:
            count += 1
            i += 1
        result += str(count) + say[i]
        i += 1

    return result

# Example: Count and Say for n = 5
n = 5
print(Count_Say(n))  # Output: '111221'