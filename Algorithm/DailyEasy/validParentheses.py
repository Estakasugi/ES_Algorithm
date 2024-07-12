def isValid(s):

    validDict = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    if ("(" not in s) and ("[" not in s) and ("{" not in s):
        return False
    if len(s) == 1:
        return False

    j = 1
    k = len(s)-1
    for i in range(len(s)):
        if s[i] not in validDict:
            j += 1
            k -= 1
            continue

        if (s[j] != validDict[s[i]]) and (s[k] != validDict[s[i]]):
            return False
        j += 1
        k -= 1 

    return True

ans = isValid(s = "){")
print(ans)