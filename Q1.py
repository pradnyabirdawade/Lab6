#1. Write a Python program to Count all letters, digits, and special symbols from the given 
#string Input = “P@#yn26at^&i5ve”Output: Chars = 8 Digits = 2 Symbol = 3 


def count_chars_digits_symbols(s):
    chars = digits = symbols = 0

    for ch in s:
        if ch.isalpha():
            chars += 1
        elif ch.isdigit():
            digits += 1
        else:
            symbols += 1

    print(f"Chars = {chars} Digits = {digits} Symbol = {symbols}")

# Test
input_str = "P@#yn26at^&i5ve"
count_chars_digits_symbols(input_str)

***Output
Chars = 8 Digits = 3 Symbol = 4
***
