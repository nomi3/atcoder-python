n = int(input())
s = list(input())
t = list(input())

if sorted(s) != sorted(t):
    print(-1)
else:
    s_i = n - 1
    for t_i in range(n - 1, -1, -1):
        if s[s_i] == t[t_i]:
            s_i -= 1
    print(s_i + 1)
