# Write your code here

def target_sum(ns, target):
    
    for x in ns:
        for y in ns:
            if x + y == target:
                return True
    
    return False

print(target_sum([1,2,3], 5)) 