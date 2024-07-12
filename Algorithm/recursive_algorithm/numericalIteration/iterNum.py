ouArr = []

def iterateNum(atMost, pos, atLeast):
    if atLeast > atMost:
        return 0
    
    for i in range(atLeast, atMost+1):
        ouArr.append(i)
        print(ouArr)
        iterateNum(atMost, pos+1, atLeast+1)

    # return iterateNum(atMost, pos, atLeast+1)

iterateNum(3, 0, 1)

    
