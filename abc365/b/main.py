N = int(input())
A = list(map(int, input().split()))

indexed_A = list(enumerate(A, start=1))

sorted_A = sorted(indexed_A, key=lambda x: x[1], reverse=True)

print(sorted_A[1][0])
