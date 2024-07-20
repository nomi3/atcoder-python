def days_until_T_or_more(N, T, P, L):
    # 現在の時点で髪の長さが T 以上の人の数をカウント
    count = sum(1 for length in L if length >= T)

    # すでに髪の長さが T 以上の人が P 人以上いる場合は 0 を出力
    if count >= P:
        return 0

    # 日数を計算
    days = 0
    while count < P:
        days += 1
        count = sum(1 for length in L if length + days >= T)

    return days

# 入力を受け取る
N, T, P = map(int, input().split())
L = list(map(int, input().split()))

# 結果を出力
print(days_until_T_or_more(N, T, P, L))