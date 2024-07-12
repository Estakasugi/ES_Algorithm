def minDifference(nums):

    if len(nums) < 3:
        return 0

    popList = []
    threeMoveCt = 3
    while threeMoveCt > 0:

        popDic = {}
        for i in range(len(nums)):
            popDic[nums[i]] = i

        currentMax = max(nums)    
        nums[popDic[currentMax]], nums[len(nums)-1] = nums[len(nums)-1], nums[popDic[currentMax]]
        popList.append(nums.pop())
        threeMoveCt -= 1

    print(nums)
    print(popList)

    if len(nums) < 2:
        return 0
    elif len(nums) == 2:
        return 1
    else:
        return min((max(nums) - min(nums)),(max(popList) - max(nums))) 


ans = minDifference(nums = [20,66,68,57,45,18,42,34,37,58])
print(ans)