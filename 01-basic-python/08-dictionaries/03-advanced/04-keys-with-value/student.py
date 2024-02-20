# Write your code here

def keys_with_value(dictionary, value):
    keys = []

    for k, v in dictionary.items():
        if v == value:
            keys.append(k)

    return keys