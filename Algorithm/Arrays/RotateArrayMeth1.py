class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k % len(nums) > 0:
            nums.reverse()
        
        left_i = 0
        if k % len(nums) > 0:
            left_j = (k-1) % len(nums)
        else:
            left_j = k % len(nums)

        print(left_i, left_j)
        while left_i < left_j:
            nums[left_i], nums[left_j] = nums[left_j], nums[left_i]
            left_i += 1
            left_j -= 1

        right_i = k % len(nums)
        if k % len(nums) > 0:
            right_j = (len(nums)-1) % len(nums)
        else:
            right_j = k % len(nums)
        print(right_i, right_j)
        while right_i < right_j:
            nums[right_i], nums[right_j] = nums[right_j], nums[right_i]
            right_i += 1
            right_j -= 1
        
        
