def min_rate_increase(R):
    if 1 <= R <= 99:
        return 100 - R
    elif 100 <= R <= 199:
        return 200 - R
    elif 200 <= R <= 299:
        return 300 - R

# 入力を受け取る
R = int(input())

# 結果を出力
print(min_rate_increase(R))