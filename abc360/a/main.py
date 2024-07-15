s = input()
rice = 0
miso = 0
for i in range(3):
    if s[i] == "R":
        rice = i
    if s[i] == "M":
        miso = i
if rice < miso:
    print("Yes")
else:
    print("No")