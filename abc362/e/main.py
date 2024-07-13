from collections import defaultdict

MOD = 998244353

N = int(input())
A = list(map(int, input().split()))

result = [0] * N
result[0] = N

if N > 1:
    result[1] = N * (N - 1) // 2

    # Aから2つ選ぶ組み合わせを辞書に格納
    base_comb = [defaultdict(int) for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            diff = A[j] - A[i]
            base_comb[j][diff] += 1

    # 等差数列の組み合わせを求める
    for k in range(2, N):
        new_comb = [defaultdict(int) for _ in range(N)]
        for i in range(N):
            for diff, count in base_comb[i].items():
                for j in range(i + 1, N):
                    if A[j] - A[i] == diff:
                        new_comb[j][diff] += count
        result[k] = sum(new_comb[i][diff] for i in range(N) for diff in new_comb[i])
        base_comb = new_comb

result = [x % MOD for x in result]
print(" ".join(map(str, result)))