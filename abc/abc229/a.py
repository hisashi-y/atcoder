S1 = input()
S2 = input()

# Noを出力するのは2パターンしかない
if (S1 == '#.' and S2 == '.#') or (S1 == '.#' and S2 == '#.'):
    print('No')
else:
    print('Yes')
