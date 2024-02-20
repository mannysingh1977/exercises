# Write your code here

def odd_keys_dict(dictonary):
    result = {}

    for k, v in dictonary.items():
        if k % 2 != 0:
            result[k] = v

    return result