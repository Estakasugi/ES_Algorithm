def isPowerThree(n):
    if n == 1:
        return True
    if (n/3) != int(n/3):
        return False
    if n == 0:
        return False
    return isPowerThree(n/3)

ans = isPowerThree(8)
print(ans)