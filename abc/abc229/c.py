# 方針: 重さあたりの美味しさが大きいチーズから使っていく
N, W = map(int, input().split())

# 単位あたりの美味しさとチーズの保持量をdictで保持する
C = {}

for i in range(N):
    a, b = map(int, input().split())
    C[a] = b

# dictのkey、つまり単位量あたりの美味しさに基づいてsortする
# a list of tuples, (単位あたりの美味しさ, 残量)
C_sorted = sorted(C.items(),reverse=True)

i = 0
ans = 0

while (W > 0) and (i <= N - 1):
    if W >= C_sorted[i][1]: #乗せられる残りの量よりもその種類のチーズが少ないなら、全部載せることができる
        ans += C_sorted[i][0] * C_sorted[i][1]
        W -= C_sorted[i][1]
    else:
        ans += W * C_sorted[i][0]
        W = 0
    i += 1

print(ans)
