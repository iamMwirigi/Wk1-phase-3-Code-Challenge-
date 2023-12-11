def solve(s):
    
    def substring_value(substring):
        return sum(ord(char) - ord('a') + 1 for char in substring)
    

    consonant_string = ''.join(char for char in s if char not in 'aeiou')
    
    substrings = consonant_string.split('a')  
    max_value = max(substring_value(substring) for substring in substrings)
    
    return max_value


print(solve("zodiacs")) 
print(solve("strength"))  
