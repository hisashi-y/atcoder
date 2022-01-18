# ナイーブなやり方、各桁の数字同士を足していって、10未満なら繰り上げがない
# アイデア候補1: 右寄せ、埋めする
# アイデア候補2: 小さい位から足していって、短い方のリストに合わせる→うまくできなかった

def judge():
    A, B = input().split()
    X, Y = A.zfill(20), B.zfill(20)
    for x, y in zip(X, Y):
        if int(x) + int(y) >= 10:
            return 'Hard'
    return 'Easy'

print(judge())
