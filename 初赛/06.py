import math

w = input().split()
w = [float(w[i]) for i in range(6)]
r = w[0]
x = w[1]
y = w[2]
S = w[3]
x0 = w[4]
y0 = w[5]
# r = 3.0
# x = 0.0
# y = 0.0
# S = 1.0
# x0 = 1.0
# y0 = 0.0

pi = 3.1415926


def func(r, x, y, S, x0, y0):
    if S > ((3 * pow(3, 0.5)) / 4) * r:
        return -1
    ds_op = pow(pow(x - x0, 2) + pow(y - y0, 2), 0.5)
    # 可以组成最大三角形的情况,直接得到三点
    if ds_op > r / 2:
        xa = x + (r / ds_op) * (x - x0)
        ya = y + (r / ds_op) * (y - y0)
        xb = xa * math.cos((2 * pi) / 3) - ya * math.sin((2 * pi) / 3)
        yb = xa * math.sin((2 * pi) / 3) + ya * math.cos((2 * pi) / 3)
        xc = xa * math.cos((4 * pi) / 3) - ya * math.sin((4 * pi) / 3)
        yc = xa * math.sin((4 * pi) / 3) + ya * math.cos((4 * pi) / 3)
        return [xa, ya, xb, yb, xc, yc]


    height = ds_op + r
    half_bottom = pow((r * r - pow(ds_op, 2)), 0.5)
    s = height * half_bottom
    if s < S:
        return -1
    res = []  # xa,ya,xb,yb,xc,yc
    xa = x + (r / ds_op) * (x - x0)
    ya = y + (r / ds_op) * (y - y0)
    delta = pi - math.acos(ds_op / r)

    xb = xa * math.cos(delta) - ya * math.sin(delta)
    yb = xa * math.sin(delta) + ya * math.cos(delta)
    xc = xa * math.cos(-delta) - ya * math.sin(-delta)
    yc = xa * math.sin(-delta) + ya * math.cos(-delta)
    return [xa, ya, xb, yb, xc, yc]


print(func(r, x, y, S, x0, y0))
