def highest_consonant_value(s):
    vowels = "aeiou"
    
    def get_consonant_value(c):
        return ord(c) - ord('a') + 1
    
    max_value = 0
    current_value = 0
    
    for char in s:
        if char not in vowels:
            current_value += get_consonant_value(char)
        else:
            max_value = max(max_value, current_value)
            current_value = 0
    

    max_value = max(max_value, current_value)
    
    return max_value

input_string = "abcde"
result = highest_consonant_value(input_string)
print(result)
