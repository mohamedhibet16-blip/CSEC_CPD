n = int(input())
wires = list(map(int, input().split()))

m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    
    x -= 1  # convert to 0-based index
    left = y - 1
    right = wires[x] - y
    if x > 0:
        wires[x - 1] += left

    if x < n - 1:
        wires[x + 1] += right
    wires[x] = 0
for birds in wires:
    print(birds)
