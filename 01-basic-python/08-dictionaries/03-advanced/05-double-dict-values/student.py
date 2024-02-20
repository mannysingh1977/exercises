# Write your code here

def double_dict_values(dictonary):
    result = {}

    for k, v in dictonary.items():
        result[k] = v * 2

    return result