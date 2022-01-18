N = int(input())

# if N < 10:
#     print('AGC00'+str(N))
# elif 10 <= N < 42:
#     print('AGC0'+str(N))
# else:
#     print('AGC0'+str(N+1))

# 別解
if N < 42:
    print('AGC'+str(N).zfill(3))
else:
    print('AGC'+str(N+1).zfill(3))
