N, T, A = map(int, input().split())

remaining_votes = N - (T + A)
if T > N // 2 or A > N // 2:
    print("Yes")
elif T + remaining_votes > N // 2 and A + remaining_votes > N // 2:
    print("No")
else:
    print("Yes")
