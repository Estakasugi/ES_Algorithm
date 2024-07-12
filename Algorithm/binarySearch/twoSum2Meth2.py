def twoSum(numbers, target):
    # result = []
    l, r = 0, len(numbers) - 1

    while l < r:
        sum_Pair = numbers[l] + numbers[r]
        if  sum_Pair < target:
            l += 1
        elif sum_Pair > target:
            r -= 1
        else:
            return [l+1, r+1]


ans = twoSum(numbers = [2,7,11,15], target = 9)
print(ans)
