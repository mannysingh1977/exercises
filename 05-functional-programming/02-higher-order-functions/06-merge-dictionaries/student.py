def merge_dictionaries(d1, d2, merge_function):
    result = dict(d1)
    for k, v in d2.items():
        if k in result:
            result[k] = merge_function(result[k], v)
        else:
            result[k] = v
    return result