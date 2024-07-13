N = int(input())
intervals = [list(map(int, input().split())) for _ in range(N)]

total_min = sum(L for L, R in intervals)
total_max = sum(R for L, R in intervals)

if total_min <= 0 <= total_max:
    print("Yes")
    current_sum = total_min
    result = []

    for L, R in intervals:
        if current_sum < 0:
            value = min(R, -current_sum + L)
        else:
            value = L
        result.append(value)
        current_sum += value - L

    print(" ".join(map(str, result)))
else:
    print("No")