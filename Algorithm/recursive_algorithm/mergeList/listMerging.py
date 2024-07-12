mergedList = []

def listMerge(list1, list2):

    # recursion
    # logic: mergedList append different items based on different situations
    if (list1 == []) and (list2 == []):
        return mergedList
    
    elif (list1 != []) and (list2 == []):
        mergedList.append(list1.pop(0))
    
    elif (list1 == []) and (list2 != []):
        mergedList.append(list2.pop(0))
        
    else:

        push1 = list1.pop(0)
        push2 = list2.pop(0)

        if push1 < push2:
            mergedList.append(push1)
            mergedList.append(push2)
        else:
            mergedList.append(push2)
            mergedList.append(push1)
        
    
    return listMerge(list1, list2)

ans = listMerge([1, 2, 4], [1,3,4])
print(ans)

