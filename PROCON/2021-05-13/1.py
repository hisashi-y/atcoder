n = int(input())
ans = 0
points = []
for i in range(n):
    point = list(map(int, input().split()))
    points.append(point)

def calc_gradient(point1, point2):
    x_delta = point2[0] - point1[0]
    y_delta = point2[1] - point1[1]
    if x_delta != 0:
        return y_delta / x_delta
    else:
        return None

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        gradient = calc_gradient(points[i], points[j])
        if gradient == None:
            continue
        elif 1 >= gradient >= -1:
            ans += 1

print(ans)
