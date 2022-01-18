S, T, X = map(int, input().split())

# 日付をまたぐかまたがないかで場合分け
if T > S: # 日付を跨がない場合
    # 電気がついているか判定
    if S <= X < T:
        print('Yes')
    else:
        print('No')
else:
    if (S <= X) or (X < T):
        print('Yes')
    else:
        print('No')
