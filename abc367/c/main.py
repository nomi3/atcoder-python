def generate_sequences(N, K, R):
    results = []

    def backtrack(sequence, current_sum):
        if len(sequence) == N:
            if current_sum % K == 0:
                results.append(sequence.copy())
            return

        for i in range(1, R[len(sequence)] + 1):
            sequence.append(i)
            backtrack(sequence, current_sum + i)
            sequence.pop()

    backtrack([], 0)
    return results


# 入力を受け取る
N, K = map(int, input().split())
R = list(map(int, input().split()))

# 数列を生成
sequences = generate_sequences(N, K, R)

# 結果を出力
if sequences:
    for seq in sequences:
        print(*seq)
else:
    print()  # 空の場合、空行を出力
