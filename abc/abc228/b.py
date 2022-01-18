def solve():
    N, X = map(int, input().split())
    A = [int(a) for a in input().split()]
    # A[i] = iが秘密を教える相手
    know = [0 for i in range(N)]
    # know[i] = 友達iが秘密を知っているか
    # know[i] = 1 知っている, 0 = 知らない
    ans = 1

    know[X - 1] = 1
    # X番目の友達(idxとしてはX - 1)は最初に秘密を教えてもらった

    now = A[X - 1] - 1
    # X番目の友達(idxとしてはX - 1)が次に秘密を教える相手

    while know[now] != 1:
        know[now] = 1
        now = A[now] - 1
        ans += 1

    print(ans)

solve()
