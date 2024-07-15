def shortestToChar(s: str, c: str):
    res = []
    c_posList = []

    for i in range(len(s)):
        if s[i] == c:
            c_posList.append(i)
    
    j = 0
    for i in range(len(s)):

        if j > 0:
            res.append(min(abs(i - c_posList[j]), abs(i - c_posList[j-1])))
        else:
            res.append(abs(i - c_posList[j]))

        if (i == c_posList[j]) and (len(c_posList) > 1):
            j += 1
    

    return res

ans = shortestToChar(s = "loveleetcode", c = "e")
print(ans)