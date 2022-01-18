def solve():
    N, X = map(int, input().split())
    A = [int(a) for a in input().split()]

    # 秘密を知ってる友人のリスト
    friends = [X]
    idx = X

    # リストに追加していく
    for i in range(len(A)):
        if A[idx-1] not in friends:
            friends.append(A[idx-1])
            idx = A[idx-1]
        else: # ループし始めたら終わる
            break

    print(len(friends))

solve()
