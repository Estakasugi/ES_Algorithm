def duplicateZeros(arr):
    """
    :type arr: List[int]
    :rtype: None Do not return anything, modify arr in-place instead.
    """
    whereToInsert = []
    for i in range(len(arr)):
        if arr[i] == 0:
            whereToInsert.append(i)


    for i in range(len(whereToInsert)):
        arr.insert(whereToInsert[i]+i, 0)
        arr.pop()
    

arrAy = [1,0,2,3,0,4,5,0]
duplicateZeros(arrAy)
print(arrAy)