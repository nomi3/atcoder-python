N = int(input())
A = list(map(int, input().split()))

result = 0
xor_count = [0] * 30  # 10^8 < 2^27 なので30ビットで十分

for i, a in enumerate(A):
    for bit in range(30):
        if a & (1 << bit):
            result += (N - i) * (1 << bit)
            xor_count[bit] = i + 1 - xor_count[bit]
        else:
            result += xor_count[bit] * (1 << bit)

print(result)
