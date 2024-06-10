n = int(input())
a = list(map(int, input().split()))
a = list(map(lambda x : x - 1, a))

vis = [False] * n
ans = [0] * n

for i in range(n):
  if vis[i]:
    continue
  b = []
  while not vis[i]:
    vis[i] = True
    b.append(i)
    i = a[i]
  if i in b:
    pos = b.index(i)
    ans[i] = len(b) - pos
    for x in b[pos:]:
      ans[x] = ans[i]
    b = b[:pos]
  t = ans[i]
  for x in b[::-1]:
    t += 1
    ans[x] = t

print(sum(ans))

