def can_afford(x, A, M):
    return sum(min(x, a) for a in A) <= M


def solve(M, A):
    if sum(A) <= M:
        return "infinite"

    left, right = 0, max(A)
    while right - left > 1:
        mid = (left + right) // 2
        if can_afford(mid, A, M):
            left = mid
        else:
            right = mid

    return left


N, M = map(int, input().split())
A = list(map(int, input().split()))

result = solve(M, A)
print(result)
