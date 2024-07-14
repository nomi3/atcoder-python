N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

d = {}
total_sum = 0
for i in range(N):
    if A[i] in d:
        if d[A[i]] > W[i]:
            total_sum += W[i]
        else:
            total_sum += d[A[i]]
            d[A[i]] = W[i]
    else:
        d[A[i]] = W[i]

print(total_sum)