import sys
import bisect

input = sys.stdin.read
data = input().split()

n = int(data[0])
q = int(data[1])
a = list(map(int, data[2 : n + 2]))
queries = data[n + 2 :]

a.sort()
result = []

index = 0
for _ in range(q):
    b = int(queries[index])
    k = int(queries[index + 1])
    index += 2

    def f(x):
        lb = bisect.bisect_left(a, b - x)
        ub = bisect.bisect_right(a, b + x)
        return (ub - lb) >= k

    ng, ok = -1, int(2e8) + 10
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if f(mid):
            ok = mid
        else:
            ng = mid

    result.append(ok)

for res in result:
    print(res)
