def solve():
    N, W = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(reverse = True, key = lambda x: x[0])

    ans = 0
    rem = W # 乗せてもいいチーズの残りの量

    for a, b in AB:
        t = min(b, rem)
        ans += a * t
        rem -= t

    return ans

print(solve())
