def reverseWords(s: str) -> str:
    stringList = s.split()
    #print(stringList)
    revList = []

    for word in stringList:

        revWord = ""
        left = 0
        right = len(word) - 1

        while left <= right:
            revWord += word[right]
            right -= 1

        revList.append(revWord + " ")
    #print(revList)
    return "".join(revList)[:-1]

ans = reverseWords(s = "Let's take LeetCode contest")
print(ans)
