def minSubArrayLen(target, nums):
    left = currSum = 0
    result = float('inf')

    for right in range(len(nums)):
        currSum += nums[right]
        while currSum > target:
            currSum -= nums[left]
            left += 1
        
        if (currSum == target):
            result = min((right - left + 1), result)

    return result if result != float('inf') else 0

ans = minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])
print(ans)