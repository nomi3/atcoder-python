def solve():
    H, W = map(int, input().split())
    Si, Sj = map(int, input().split())
    grid = [input() for _ in range(H)]
    X = input()

    # 現在の位置
    i, j = Si - 1, Sj - 1  # 0-indexedに変換

    # 移動方向
    moves = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

    for direction in X:
        di, dj = moves[direction]
        ni, nj = i + di, j + dj

        # 新しい位置が有効で、空きマスであれば移動
        if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] == '.':
            i, j = ni, nj

    # 1-indexedに戻して出力
    print(i + 1, j + 1)

solve()
