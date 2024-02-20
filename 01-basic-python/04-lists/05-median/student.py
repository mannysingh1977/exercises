# Write your code here

def median(ns):
    ns.sort()

    if len(ns) % 2 == 1:
        return ns[len(ns) // 2]
    
    else:
        middle1 = ns[len(ns) // 2 - 1]
        middle2 = ns[len(ns) // 2]

        return (middle1 + middle2) / 2

print(median([1,4,5,3,2]))