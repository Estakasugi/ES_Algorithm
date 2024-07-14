def numSubarrayProductLessThanK(nums, k) -> int:

    if k <= 1:
        return 0

    left = ans = 0
    curr = 1
    for i in range(len(nums)):
        curr *= nums[i]

        while curr >= k:
            curr //= nums[left]
            left += 1

        ans += i - left + 1

    return ans

ans = numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100)
print(ans)