def addBinary(a, b):
    result = bin(int(a, 2) + int(b, 2))
    return result[2:]

ans = addBinary(a = "101", b = "1010")
print(ans)