#Q2 Write a Python program to remove duplicate characters of a given string. 
#Input = “String and String Function” Output: String and Function

def remove_duplicate_words(s):
    words = s.split()
    unique_words = []
    
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    
    return ' '.join(unique_words)

# Test
input_str = "String and String Function"
output_str = remove_duplicate_words(input_str)
print(output_str)

***Output
String and Function
***
