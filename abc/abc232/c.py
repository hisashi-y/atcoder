from itertools import permutations

def judge():
    N, M = map(int, input().split())
    #高橋君の隣接行列
    AB = [[0] * N for _ in range(N)]
    #青木君の隣接行列
    CD = [[0] * N for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        #a, bの値と隣接行列のidxは一つずつズレているので
        a, b = a - 1, b - 1
        AB[a][b] = 1
        AB[b][a] = 1

    for _ in range(M):
        c, d = map(int, input().split())
        #c, dの値と隣接行列のidxは一つずつズレているので
        c, d = c - 1, d - 1
        CD[c][d] = 1
        CD[d][c] = 1

    def is_the_same_shape(perm):
        for i in range(N):
            for j in range(N):
                if AB[i][j] != CD[perm[i]][perm[j]]:
                    return False
        return True

    for perm in permutations(range(N)):
        if is_the_same_shape(perm):
            return True
    return False

print('Yes' if judge() else 'No')
