n = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = [i for i in a if i not in n]

if len(ans) == 0:
    print('')
else:
    print(*ans)
