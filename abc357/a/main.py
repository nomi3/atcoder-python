N, M = map(int, input().split())
H = list(map(int, input().split()))
count = 0
current = M
for h in H:
    if current >= h:
        count += 1
        current = current - h
    else:
        break
print(count)