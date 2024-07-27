N = int(input())
dishes = [input() for _ in range(N)]

can_eat_all = True
sweet_count = 0

for dish in dishes[:-1]:
    if dish == 'sweet':
        sweet_count += 1
        if sweet_count == 2:
            can_eat_all = False
            break
    else:
        sweet_count = 0

if can_eat_all:
    print('Yes')
else:
    print('No')