def checkIfExist(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    doubleDictionary = {}
    for num in arr:
        doubleDictionary[num] = True
    
    zeroCt = 0
    for num in arr:
        if (2 * num in doubleDictionary) and (num!=0):
            print(num)
            return True

        if (num == 0) and (zeroCt == 0):
            zeroCt += 1
            continue
        
        if (num == 0) and (zeroCt == 1):
            return True

    return False

ans = checkIfExist([-2,0,10,-19,4,6,-8])
ans2 = checkIfExist([0, 0])
print(ans2)