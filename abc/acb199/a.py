n = int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))

ans_set = {}
for i in range(n):
    temp_set = {}
    if i == 0:
        ans_set = set(list(range(a[i], b[i]+1)))
    else:
        temp_set = set(list(range(a[i], b[i]+1)))
        ans_set = ans_set & temp_set

print(len(ans_set))
