R, G, B = map(int, input().split())
C = input()

# 高橋君が嫌いな色によって買えるペンの色を決める
if C == "Red":
    min_cost = min(G, B)
elif C == "Green":
    min_cost = min(R, B)
elif C == "Blue":
    min_cost = min(R, G)

# 結果の出力
print(min_cost)