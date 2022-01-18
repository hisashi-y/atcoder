# 方針: 4日目にK位以内に入ることができない
# -> 他の人は4日目で0点(つまり3日目までの点数の合計しか持っていない)、自分は4日目で300点獲得
# このような状況であってもK位以内に入っていないのなら、K位以内に入ることは有り得ない
# 逆に、このような状況でK位以内に入れるなら有りえると言える

def solve():
    N, K = map(int, input().split())
    # これまでの生徒の3日目までの得点
    scores = [sum(map(int, input().split())) for i in range(N)]
    border = sorted(scores, reverse=True)[K - 1]
    for score in scores:
        if score + 300 >= border:
            print('Yes')
        else:
            print('No')
solve()
