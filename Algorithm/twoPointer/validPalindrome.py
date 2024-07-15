class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = "".join(char for char in s if char.isalnum()).lower()

        i = 0
        j = len(cleanString) - 1

        while i < j:
            if cleanString[i] != cleanString[j]:
                return False
            i += 1
            j -= 1

        return True
