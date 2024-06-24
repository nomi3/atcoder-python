sx, sy = map(int, input().split())
tx, ty = map(int, input().split())
# 距離の絶対値を求める
dx = abs(tx - sx)
dy = abs(ty - sy)
if dy >= dx:
    print(dy)
else:
    if tx > sx:
        if (sx + sy)%2 == 0:
            print((dx-dy)//2+dy)
        else:
            print((dx-dy+1)//2+dy)
    else:
        if (sx + sy)%2 == 0:
            print((dx-dy+1)//2+dy)
        else:
            print((dx-dy)//2+dy)