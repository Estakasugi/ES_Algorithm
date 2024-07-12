def findDiagonalOrder(mat):
    j = len(mat) - 1
    for i in range(len(mat[0])-1, -1, -1):
        print(mat[j][i])
        j -= 1

ans = findDiagonalOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print(ans)