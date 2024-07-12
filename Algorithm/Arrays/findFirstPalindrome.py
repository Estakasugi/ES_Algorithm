def firstPalindrome(words) -> str:
    
    for word in words:

        isPalindrome = True

        if len(word) == 1:
            return word

        left = 0
        right = len(word) - 1
       
        while left < right:
            # print(word[left], word[right])
            if word[left] != word[right]:
                isPalindrome = False
                break
            
            left += 1
            right -= 1

        if isPalindrome:
            return word
    
    return ""

ans = firstPalindrome(["dwcblqnxtrwtqmtqenidhxnifdbmdvobwmcvwjxgbyjzgvrqzlskjbfirauguhyyjhlotuckssrkqzppzbqd"])
print(ans)