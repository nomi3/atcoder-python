def solve(N, P, Q):
    # マス目を作成し、初期化
    grid = [[None] * N for _ in range(N)]

    for i in range(N):
        # P[i]行目の空いているマスに0を書き込む
        for j in range(N):
            if grid[P[i] - 1][j] is None:
                grid[P[i] - 1][j] = 0

        # Q[N-1-i]列目の空いているマスに1を書き込む
        for j in range(N):
            if grid[j][Q[N - 1 - i] - 1] is None:
                grid[j][Q[N - 1 - i] - 1] = 1

    # 結果を出力
    for row in grid:
        print("".join(map(str, row)))


# 入力を受け取る
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# 問題を解く
solve(N, P, Q)
