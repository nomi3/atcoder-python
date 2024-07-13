n, k, x = map(int, input().split())
a = list(map(int, input().split()))

# aのk番目のにxを挿入
a.insert(k, x)

# aを半角スペース区切りで出力
print(*a)