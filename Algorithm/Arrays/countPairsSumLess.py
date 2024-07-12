def countPairs(nums, target):
    
    nums.sort()

    res = 0
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] < target:
            res += (j-i)
            i += 1
        
        if nums[i] + nums[j] >= target:
            j -= 1


    return res

ans = countPairs(nums = [-6,2,5,-2,-7,-1,3], target = -2)
print(ans)