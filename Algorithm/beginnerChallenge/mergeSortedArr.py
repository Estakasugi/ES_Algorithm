def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    for i in range(len(nums1)):
        if i >= m:
            nums1.pop()
    
    for j in range(len(nums2)):
        if j >= n:
            nums2.pop()
    
    nums1 += nums2
    nums1.sort()
    

arr1 = [0]
m = 0
arr2 = [1]
n = 1

merge(arr1, m, arr2, n)

print(arr1)
