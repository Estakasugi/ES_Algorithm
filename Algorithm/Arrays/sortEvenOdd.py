def sortArrayByParity(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    j = 0
    for i in range(1, len(nums)):
        if (nums[i] % 2 == 0) and (nums[j] % 2 != 0):
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
        
        if (nums[j] % 2 == 0):
            j += 1

    return nums  

nums = [0]
ans = sortArrayByParity(nums)
print(ans)