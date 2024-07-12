def fibNum(nthNumb):
    if nthNumb == 0:
        return 0
    if nthNumb == 1:
        return 1
    return fibNum(nthNumb-1) + fibNum(nthNumb-2)

ans = fibNum(12)
print(ans)