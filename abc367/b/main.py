X = float(input())

# 小数点以下の桁数を確認
decimal_part = str(X).split(".")[1] if "." in str(X) else ""
decimal_places = len(decimal_part.rstrip("0"))

if decimal_places == 0:
    print(int(X))
else:
    print(f"{X:.{decimal_places}f}")
