def minimumAverage(nums) -> float:
    
    averages = []
    nums.sort()
    print(nums)

    left = 0
    right = len(nums) - 1
    while left < right:
        averages.append((nums[left] + nums[right]) / 2)
        left += 1
        right -= 1

    return min(averages)

ans = minimumAverage(nums = [1,2,3,7,8,9])
print(ans)
