N = int(input())
S = input()

MOD = 10**9 + 7

current_char = S[0]
renzoku_count = 1
sum = 1

for i in range(1, N):
    if S[i] != current_char:
        renzoku_count += 1
    if S[i] == current_char or i == N-1:
        if renzoku_count % 2 == 0:
            sum = (sum * (renzoku_count // 2)) % MOD
        else:
            sum = (sum * (renzoku_count // 2 + 1)) % MOD
        renzoku_count = 1
    current_char = S[i]

result = sum % MOD

print(result)