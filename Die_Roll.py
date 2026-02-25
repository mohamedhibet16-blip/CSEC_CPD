Y, W = map(int, input().split())

m = max(Y, W)
favorable = 6 - m + 1
denominator = 6

if favorable == 6:
    print("1/1")
elif favorable == 3:
    print("1/2")
elif favorable == 4:
    print("2/3")
elif favorable == 2:
    print("1/3")
else:
    print(f"{favorable}/6")
