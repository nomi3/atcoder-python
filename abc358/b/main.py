n, a = map(int, input().split())
t = list(map(int, input().split()))
finish_time = [0] * n
finish_time[0] = t[0] + a
for i in range(1, n):
    if t[i] > finish_time[i-1]:
        finish_time[i] = t[i] + a
    else:
        finish_time[i] = finish_time[i-1] + a
for i in range(n):
    print(finish_time[i])