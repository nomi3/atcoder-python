from collections import defaultdict

Q = int(input())
bag = defaultdict(int)
unique_numbers = set()

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]
        bag[x] += 1
        unique_numbers.add(x)

    elif query[0] == 2:
        x = query[1]
        bag[x] -= 1
        if bag[x] == 0:
            unique_numbers.remove(x)

    else:  # query[0] == 3
        print(len(unique_numbers))
