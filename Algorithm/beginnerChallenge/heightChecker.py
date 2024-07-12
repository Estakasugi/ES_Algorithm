def heightChecker(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    originalHeights = heights[:]
    heights.sort()
    diff = 0

    print(originalHeights)
    print(heights)

    for i in range(len(originalHeights)):
        if originalHeights[i] != heights[i]:
            diff += 1

    return diff

ans = heightChecker([1,1,4,2,1,3])
# ans2 = heightChecker([5,1,2,3,4])
# ans3 = heightChecker([1,2,3,4,5])
print(ans)