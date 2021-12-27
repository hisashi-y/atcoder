import string
lst = list(string.ascii_lowercase)

S = input()
T = input()

#1st step: K を決める
#lstの最初に戻らないような場合
S_1st_idx = lst.index(S[0])
T_1st_idx = lst.index(T[0])
if T_1st_idx - S_1st_idx >= 0:
    K = T_1st_idx - S_1st_idx
else:
    K = T_1st_idx - S_1st_idx + len(lst)

def character_shift(S, K):
    shifted = ''
    for character in S:
        shifted += lst[(lst.index(character) + K) % 26]
    return shifted

if character_shift(S, K) == T:
    ans = 'Yes'
else:
    ans = 'No'

print(ans)
