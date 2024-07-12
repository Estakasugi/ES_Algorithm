import math
def isPowerOfThree(n):
    if n <= 0:
        return False
    
    logThree = math.log(n,3)
    if logThree == int(logThree):
        return True
    else:
        return False

ans = isPowerOfThree(-1)
print(ans)
