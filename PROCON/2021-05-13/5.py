import math

n = int(input())
t = input()
len_s = 30000000000
#sは長いのでtに対して十分な長さを持つsubstringを考える
lcm = math.lcm(len(t), 3)

s_sub = '110' * (lcm)
sub_count = s_sub.count(t)
ans = sub_count * (len_s / lcm)
print(ans)
