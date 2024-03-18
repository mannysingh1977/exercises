# Write your code here
import re

def remove_trailing_whitespace(string):
    return re.sub(r'\s+$', '', string, flags=re.MULTILINE)

print(f'"{remove_trailing_whitespace("Hello, World!  ")}"')
print(f'"{remove_trailing_whitespace("  Hello, World!  ")}"')
