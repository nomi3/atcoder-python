# 入力の読み込み
xA, yA = map(int, input().split())
xB, yB = map(int, input().split())
xC, yC = map(int, input().split())

# ベクトルの内積を用いて直角を判定する関数
def is_right_angle(ax, ay, bx, by, cx, cy):
    # ベクトル AB と ベクトル AC の内積が 0 ならば直角
    ABx = bx - ax
    ABy = by - ay
    ACx = cx - ax
    ACy = cy - ay
    dot_product1 = ABx * ACx + ABy * ACy

    # ベクトル BA と ベクトル BC の内積が 0 ならば直角
    BAx = ax - bx
    BAy = ay - by
    BCx = cx - bx
    BCy = cy - by
    dot_product2 = BAx * BCx + BAy * BCy

    # ベクトル CA と ベクトル CB の内積が 0 ならば直角
    CAx = ax - cx
    CAy = ay - cy
    CBx = bx - cx
    CBy = by - cy
    dot_product3 = CAx * CBx + CAy * CBy

    return dot_product1 == 0 or dot_product2 == 0 or dot_product3 == 0

# 直角かどうかの判定
if is_right_angle(xA, yA, xB, yB, xC, yC):
    print("Yes")
else:
    print("No")