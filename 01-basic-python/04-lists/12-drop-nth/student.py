# Write your code here

def drop_nth(xs, n):
    
    return xs[:n] + xs[n+1:]


print(drop_nth([1,2,3,4,5,6,7], 2))