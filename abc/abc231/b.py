N = int(input())

candidates = {}

for _ in range(N):
    S_i = input()
    candidates[S_i] = candidates.get(S_i, 0) + 1

ans = max(candidates, key = candidates.get)
print(ans)
