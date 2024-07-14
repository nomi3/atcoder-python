def count_crossings(N, T, S, X):
    ants = [(X[i], S[i]) for i in range(N)]
    ants.sort()  # 蟻の位置でソート

    right_ants = []  # 正の方向に進む蟻のリスト
    crossing_count = 0

    for position, direction in ants:
        if direction == '1':
            right_ants.insert(0, position)
        else:
            # 左向きの蟻が見つかったら、右向きの蟻とのすれ違いをカウント
            while right_ants and right_ants[-1] + 2 * T < position:
                right_ants.pop()  # すれ違わない蟻をリストから削除
            crossing_count += len(right_ants)

    return crossing_count

N, T = map(int, input().split())
S = input()
X = list(map(int, input().split()))

# 結果の出力
result = count_crossings(N, T, S, X)
print(result)