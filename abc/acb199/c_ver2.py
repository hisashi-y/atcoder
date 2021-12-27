n = int(input())
s = list(input())
q = int(input())

t_count = False
for i in range(q):
    t, a, b = map(int, input().split())
    if t == 2:
        t_count = not t_count
    else:
        if t_count == True:
            if b <= n:
                s[a - 1 + n], s[b - 1 + n] = s[b - 1 + n], s[a - 1 + n]
            elif b > n and a <= n:
                s[a - 1 + n], s[b - 1 - n] = s[b - 1 - n], s[a - 1 + n]
            elif b > n and a > n:
                s[a - 1 - n], s[b - 1 - n] = s[b - 1 - n], s[a - 1 - n]
        else:
            s[a - 1], s[b - 1] = s[b - 1], s[a - 1]

if t_count == True:
    latter = s[n:]
    former = s[:n]
    s = latter + former

print(''.join(s))
