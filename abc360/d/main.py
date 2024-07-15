def count_crossings(N, T, S, X):
    ants = [(X[i], S[i]) for i in range(N)]
    ants.sort()  # 蟻の位置でソート

    right_ants = []  # 正の方向に進む蟻の位置を保持するリスト
    crossing_count = 0
    j = 0  # 右向きの蟻の範囲を管理するポインタ

    for i in range(N):
        position, direction = ants[i]
        if direction == '1':
            right_ants.append(position)
        else:
            # 左向きの蟻が見つかったら、右向きの蟻とのすれ違いをカウント
            while j < len(right_ants) and right_ants[j] + 2 * T < position:
                j += 1  # 範囲外の右向きの蟻をスキップ
            crossing_count += len(right_ants) - j

    return crossing_count

# 入力の受け取り
N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))

# 結果の出力
result = count_crossings(N, T, S, X)
print(result)