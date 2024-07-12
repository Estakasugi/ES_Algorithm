def relativeSortArray(arr1, arr2):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :rtype: List[int]
    """

    arr1EleCountDictionary = {}
    for i in range(len(arr1)):
        if arr1[i] in arr1EleCountDictionary:
            arr1EleCountDictionary[arr1[i]] += 1
        else:
            arr1EleCountDictionary[arr1[i]] = 1


    arr2PosDictionary = {}
    for i in range(len(arr2)):
        arr2PosDictionary[arr2[i]] = i


    nonArr2List = []
    for num in arr1:
        if num not in arr2PosDictionary:
            nonArr2List.append(num)
    nonArr2List.sort()


    arr2IncludeList = []
    for num in arr2:
        for i in range(arr1EleCountDictionary[num]):
            arr2IncludeList.append(num)



    return arr2IncludeList + nonArr2List

ans = relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6])
ans2 = relativeSortArray([28,6,22,8,44,17], [22,28,8,6])
print(ans2)