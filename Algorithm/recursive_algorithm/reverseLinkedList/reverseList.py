revList = []

def listReverse(list):

    if list == []:
        return revList
    else:
        revList.append(list.pop())
        return listReverse(list)

ans = listReverse([1, 2, 3, 4, 5])
print(ans)