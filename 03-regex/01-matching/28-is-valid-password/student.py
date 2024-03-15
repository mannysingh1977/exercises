# Write your code here
import re

def is_valid_password(string):
    positive = [
        r'.{12,}',
        r'[0-9]',
        r'[a-z]',
        r'[A-Z]',
        r'[-+/*.@]',
    ]

    negative = [
        r'(.)\1{2}',
        r'(.)(.*\1){3}'
    ]

    for regex in positive:
        if not re.search(regex, string):
            return False
        
    for regex in negative:
        if re.search(regex, string):
            return False
    
    return True