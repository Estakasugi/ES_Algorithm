class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        curr = str(num)[:k]

        if num % int(curr, 10) == 0:
            res += 1 

        for i in range(k, len(str(num))):
            curr += str(num)[i]
            curr = curr[-k:]
            
            if int(curr, 10) == 0:
                continue

            if num % int(curr, 10) == 0:
                res += 1 

        return res
