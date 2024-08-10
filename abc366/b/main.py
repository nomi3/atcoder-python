N = int(input())
S = [input() for _ in range(N)]

M = max(len(s) for s in S)
T = [""] * M

for i in range(M):
    column = ""
    for j in range(N - 1, -1, -1):
        if i < len(S[j]):
            column += S[j][i]
        else:
            column += "*"
    T[i] = column.rstrip("*")

for t in T:
    print(t)
