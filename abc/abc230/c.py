N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())


for i in range(P, Q+1):
    ans = ''
    for j in range(R, S+1):
        if (i - j - A + B == 0) or (i + j - A - B == 0):
            ans += '#'
        else:
            ans += '.'
    print(ans)
