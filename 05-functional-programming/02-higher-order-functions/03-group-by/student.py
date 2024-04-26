def group_by(xs, key_function):
    res = {}

    for x in xs:
        key = key_function(x)
        if key not in res:
            res[key] = []
        res[key].append[x]
    return res