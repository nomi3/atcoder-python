def janken(a, b):
    if a == b:
        return 0
    if (a == "R" and b == "S") or (a == "S" and b == "P") or (a == "P" and b == "R"):
        return 1
    return -1


def solve(N, S):
    dp = [[0] * 3 for _ in range(N + 1)]
    hands = {"R": 0, "P": 1, "S": 2}

    for i in range(1, N + 1):
        aoki_hand = S[i - 1]
        for h in hands:
            result = janken(h, aoki_hand)
            if result == -1:
                dp[i][hands[h]] = 0
            elif result == 0:
                dp[i][hands[h]] = max(dp[i - 1][j] for j in range(3) if j != hands[h])
            else:
                dp[i][hands[h]] = 1 + max(
                    dp[i - 1][j] for j in range(3) if j != hands[h]
                )

    return max(dp[N])


N = int(input())
S = input()
print(solve(N, S))
