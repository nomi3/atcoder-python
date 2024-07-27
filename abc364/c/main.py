N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

sweet_sum = 0
salty_sum = 0
count = 0

for i in range(N):
    sweet_sum += A[i]
    salty_sum += B[i]
    count += 1
    if sweet_sum > X or salty_sum > Y:
        break

print(count)