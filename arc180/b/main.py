n, k = map(int, input().split())
p = list(map(int, input().split()))

# r-l >= k, p[l] > p[r]という条件を満たしつつ
# swapのl側はなるべくp[l]が小さくなるように、r側はなるべくp[r]が大きくなるようにえらんでいく

res = []

head = [(p[i], i) for i in range(n-k)]
head.sort()

for _, i in head: # p[i]が最小のものから順に見ていく
    # r-l >= k, p[l] > p[r]という条件を満たすものを列挙する
    arr = [(p[j], j) for j in range(i+k, n) if p[j] < p[i]]
    # p[r]が大きい順に並べる
    arr.sort(reverse=True)

    # swapする操作を記録する
    b = [j for _, j in arr]
    res.extend([(i+1, j+1) for j in b])

    # swapした結果をpに反映する
    val = [p[i]] + [p[j] for j in b]
    for v, j in zip(val, b + [i]):
        p[j] = v

print(len(res))
for i, j in res:
    print(i, j)

# 計算量
# headの各要素に対してn-k回のループがあるので、最悪の場合O(n)回のループが実行される
# arrのソートで、arrの要素は最悪nに近い値を取ることがあるため、O(n log n)となる
# よって、全体の計算量はO(n^2 log n)となる