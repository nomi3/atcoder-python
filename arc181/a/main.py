def solve(N, P):
    # Pの最初の値と最後の値を取得
    first = P[0]
    last = P[-1]

    # Pのkey-valueを転置
    inv_P = [0] * (N + 1)
    for i, v in enumerate(P, 1):
        inv_P[v] = i

    # 最初からPが昇順に並んでいる場合
    if inv_P[1:] == list(range(1, N + 1)):
        return 0
    # 最初からPが降順に並んでいる場合
    if inv_P[1:] == list(range(N, 0, -1)):
        return 3

    # P[k]=kかつP[1]からP[k-1]に1からk-1が全て含まれている場合
    max_seen = 0
    for k in range(1, N + 1):
        max_seen = max(max_seen, inv_P[k])
        if inv_P[k] == k and max_seen == k:
            return 1

    # その他の場合
    if first == N and last == 1:
        return 3
    return 2


T = int(input())
for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))
    print(solve(N, P))
