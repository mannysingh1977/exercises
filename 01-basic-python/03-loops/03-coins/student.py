# Write your code here

def coins(one, two, five, goal):
    
    if goal < 1 or (goal - one * 1 - two * 2 - five * 5) > 0:
        return False
    
    for i in range(one + 1):
        for j in range(two + 2):
            for k in range(five + 5):
                totalcoins = i + j *2 + k * 5

                if totalcoins == goal:
                    return True
    
    return False
    