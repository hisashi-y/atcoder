n = int(input())
s = list(input())
q = int(input())

t_count = False
for i in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        if t_count == False:
            s[a - 1], s[b - 1] = s[b - 1], s[a - 1]
        else:
            if b <= n:
                b_idx = b - 1 + n
                a_idx = a - 1 + n
            else:
                b_idx = b - 1 - n
                if a <= n:
                    a_idx = a - 1 + n
                else:
                    a_idx = a - 1 - n
            s[a - 1], s[b - 1] = s[b_idx], s[a_idx]
    else:
        t_count = not t_count

if t_count == True:
    latter = s[n:]
    former = s[:n]
    s = latter + former

print(''.join(s))
