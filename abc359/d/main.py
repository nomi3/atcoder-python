# Sの1文字目から順に見ていく。
# K-1文字目までは?をAとBのどちらかで埋めたすべての文字列をキーとして持つ辞書mpを用意しておく。
# K文字目以降は、mpのキーの末尾にありうる文字を追加して新たなキーを作る。
# ただし、回文になるような文字列については、キーから削除する。
# 回文にならない文字は、次の文字を追加するために先頭の文字を削除して新たなキーを作る。

N, K = map(int, input().split())

S = input()

# Sの一文字目を見て、AかBか?で、dpの初期値を設定する
if S[0] == 'A':
    dp = {'A': 1}
elif S[0] == 'B':
    dp = {'B': 1}
else:
    dp = {'A': 1, 'B': 1}

# K-1文字目までを見ていく
for i in range(1, K-1):
    tmp = {}
    for s, v in dp.items():
        if S[i] == 'A':
            tmp[s + 'A'] = v
        elif S[i] == 'B':
            tmp[s + 'B'] = v
        else:
            tmp[s + 'A'] = v
            tmp[s + 'B'] = v
    dp = tmp

# K文字目以降を見ていく
for i in range(K-1, N):
    tmp = {}
    for s, v in dp.items():
        if S[i] == 'A':
            tmp[s + 'A'] = v
        elif S[i] == 'B':
            tmp[s + 'B'] = v
        else:
            tmp[s + 'A'] = v
            tmp[s + 'B'] = v
    dp = {}
    for s, v in tmp.items():
        if s != s[::-1]:
            if s[1:] in dp:
                dp[s[1:]] += v
            else:
                dp[s[1:]] = v

# 答えは、dpの値の合計を998244353で割った余り
print(sum(dp.values()) % 998244353)