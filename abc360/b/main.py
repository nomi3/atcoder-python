S, T = input().split()

len_S = len(S)
len_T = len(T)

for w in range(1, len_S):
    parts = []
    # 分割
    for i in range(0, len_S, w):
        part = S[i:i+w]
        parts.append(part)
    for j in range(w):
        concatenated = []
        for part in parts:
            if len(part) > j:
                concatenated.append(part[j])

        if ''.join(concatenated) == T:
            print("Yes")
            exit()

print("No")


