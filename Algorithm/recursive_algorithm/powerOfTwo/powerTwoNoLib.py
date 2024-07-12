def powerTwoTest (n):
    
    if int(n) == 1:
        return True
    if n/2 != int(n/2):
        return False

    return powerTwoTest(n/2) 

ans = powerTwoTest(3)
print(ans)