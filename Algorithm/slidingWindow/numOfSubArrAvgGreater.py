class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr = res_count = 0
        for i in range(k):
            curr += arr[i]
        
        if curr >= threshold * k:
            res_count += 1

        for i in range(k, len(arr)):
            curr += (arr[i] - arr[i - k])

            if curr >= threshold * k:
                res_count += 1

        return res_count