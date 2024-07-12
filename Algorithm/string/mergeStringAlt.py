def mergeAlternately(word1: str, word2: str) -> str:

    res = ""
    i = j = 0

    while (i < len(word1) ) and (j < len(word2) ):
        res += word1[i]
        res += word2[j]
        i += 1
        j += 1
    
    while i < len(word1):
        res += word1[i]
        i += 1

    while j < len(word2):
        res += word2[j]
        j += 1
    

    return res

ans = mergeAlternately(word1 = "ab", word2 = "pqrs")
print(ans)