A, B, C = map(int, input().split())

if B < C:
    # 就寝時間が起床時間より前の場合
    if A >= C or A < B:
        print("Yes")
    else:
        print("No")
else:
    # 就寝時間が起床時間より後の場合（日をまたぐ）
    if A >= C and A < B:
        print("Yes")
    else:
        print("No")
