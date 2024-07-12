def twoSum(numbers, target):
    result = []
    targetDict = {}
    doubleEle = 0

    for i in range(len(numbers)):
        if target - numbers[i] == numbers[i]: 
            doubleEle += 1
        targetDict[target - numbers[i]] = i


    for i in range(len(numbers)):
        if (numbers[i] in targetDict):
            if target - numbers[i] != numbers[i]:
                result.append(i+1)
            else:
                if doubleEle % 2 == 0:
                    result.append(i+1)

    return result

ans = twoSum(numbers = [2,3,4], target = 6)
print(ans)

