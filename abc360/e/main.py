def mod_inv(a, p):
    return pow(a, p - 2, p)

def expected_position_mod(N, K, MOD):
    # 初期期待値
    dp_num = [0] * (K + 1)  # 分子
    dp_den = [0] * (K + 1)  # 分母
    dp_num[0] = 1
    dp_den[0] = 1

    # 期待値の計算
    for i in range(K):
        # dp[i+1] = dp[i]*(N - 2)/N + (N+1)/N
        # 期待値の求め方は、https://atcoder.jp/contests/abc360/editorial/10352
        dp_num[i + 1] = (dp_num[i] * (N - 2) + dp_den[i] * (N + 1)) % MOD
        dp_den[i + 1] = (dp_den[i] * N) % MOD


    P = dp_num[K]
    Q = dp_den[K]

    # Q の逆元を計算
    Q_inv = mod_inv(Q, MOD)

    # 最終結果 R の計算
    R = (P * Q_inv) % MOD

    return R

# 入力
N, K = map(int, input().split())
MOD = 998244353

# 期待値のmodを計算して出力
result = expected_position_mod(N, K, MOD)
print(result)