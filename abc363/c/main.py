from collections import Counter
from math import factorial

def factorial_divide(n, counts):
    result = factorial(n)
    for count in counts:
        result //= factorial(count)
    return result

def count_k_palindrome_free_permutations(N, K, S):
    count = Counter(S)
    unique_chars = list(count.keys())

    memo = {}

    def dp(remaining, path_length, last_chars):
        state = (tuple(remaining), path_length, tuple(last_chars))
        if state in memo:
            return memo[state]

        if path_length == N:
            return 1

        total = 0
        for idx, char in enumerate(unique_chars):
            if remaining[idx] > 0:
                new_last_chars = last_chars + [char]
                if len(new_last_chars) > K:
                    new_last_chars.pop(0)

                if len(new_last_chars) < K or new_last_chars != new_last_chars[::-1]:
                    new_remaining = list(remaining)
                    new_remaining[idx] -= 1
                    total += dp(new_remaining, path_length + 1, new_last_chars)

        memo[state] = total
        return total

    initial_remaining = [count[char] for char in unique_chars]
    return dp(initial_remaining, 0, [])

# 入力
N, K = map(int, input().split())
S = input().strip()

# Sの中身が全て違う文字で構成されている場合は、N!通りの並べ方が存在する
if len(set(S)) == N:
    print(factorial(N))
    exit()

# 出力
print(count_k_palindrome_free_permutations(N, K, S))