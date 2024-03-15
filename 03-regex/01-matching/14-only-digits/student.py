# Write your code here
import re

def only_digits(string):
    return re.fullmatch('[01234456789]*', string)