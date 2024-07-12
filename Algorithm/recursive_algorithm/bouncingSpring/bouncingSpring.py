def recSpring(n, array):
    if (array[0] + 1) > len(array):
        return 1
    return recSpring(n-array[0], array[array[0]:]) + 1

ans = recSpring(5, [2, 2, 3, 1, 2])
print(ans)