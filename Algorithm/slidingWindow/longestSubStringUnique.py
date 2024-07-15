class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dupt_Dict = {}
        left = res = 0

        for right in range(len(s)):

            if s[right] not in dupt_Dict:
                dupt_Dict[s[right]] = 1
            else:
                dupt_Dict[s[right]] += 1
            
            while dupt_Dict[s[right]] > 1:
                
                dupt_Dict[s[left]] = 0
                left += 1

            dupt_Dict[s[right]] = 1

            res = max(res, right - left + 1)

        return res
