import math

# print(4 **(1/2))
def powerTwoTest (n):

    if math.log2(n) != int(math.log2(n)):
        return False
    else: 
        return True

ans = powerTwoTest(18)
print(ans)