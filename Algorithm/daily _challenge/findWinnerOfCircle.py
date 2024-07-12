def findTheWinner(n, k):
    nums = []
    for i in range(1,n+1):
        nums.append(i)

    outDict = []
    while len(outDict) < n-1:
        outDict.append(nums[ (k-1) % len(nums) ])
        nums = nums[(k% len(nums)):] + nums[:(k% len(nums))]
        nums.pop()
        print(nums, outDict)


    return nums[0]

ans = findTheWinner(n = 5, k = 2)
print(ans)