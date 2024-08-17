N = int(input())
A = list(map(int, input().split()))
ans = 0
A_MAX = 10**8
BIT_LEN = len(f"{A_MAX:b}")  # 2進数化して桁数
for i in range(BIT_LEN):  # iビット目
    acc = 0  # 累積和
    cnt_0, cnt_1 = 1, 0  # 累積XORを求める際の0と1の数
    cnt_ai = 0  # 配列Aのiビット目の1の数を数えておく
    for a in A:
        v = (a >> i) & 1  # iビット目の値(0 or 1)
        cnt_ai += v  # iビット目の1の数を数えておく
        acc ^= v
        if acc == 0:
            cnt_0 += 1
        else:
            cnt_1 += 1
    ans += (cnt_0 * cnt_1 - cnt_ai) * (1 << i)
print(ans)
