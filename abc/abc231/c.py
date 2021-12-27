import pep8

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()


def binary_search(x):
    # x ≦ A[0]の時全ての人がxより大きいのでlen(A) = Nを返す
    if x <= A[0]:
        return N

    # A[-1] < xの時xより大きい人は存在しないので0を返す
    elif A[-1] < x:
        return 0

    # comments test
    left = 0
    # comments test
    right = N-1

    while 1 < right - left:
        center = (left + right)//2

        if A[center] < x:
            left = center
        else:
            right = center

    return N - right


for i in range(Q):
    x = int(input())
    print(binary_search(x))
