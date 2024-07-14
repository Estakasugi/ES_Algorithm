def findMaxAverage(nums, k: int) -> float:
    ans = 0
    curr = 0
    for i in range(k):
        curr += nums[i]
    
    ans = curr

    for i in range(k,len(nums)):
        curr += (nums[i]-nums[i-k])
        ans = max(curr, ans)

    
    return ans / k

ans = findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4)
print(ans)