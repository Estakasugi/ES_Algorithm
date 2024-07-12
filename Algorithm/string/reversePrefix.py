def reversePrefix(word: str, ch: str) -> str:
    revList = []
    right = 0
    left = 0

    for char in word:
        revList.append(char)


    for i in range(len(revList)):
        if revList[i] == ch:
            right = i
            break
    
    while right > left:
        revList[left], revList[right] = revList[right], revList[left]
        left += 1
        right -= 1

    return "".join(revList)

ans = reversePrefix(word = "abcd", ch = "z")
print(ans)