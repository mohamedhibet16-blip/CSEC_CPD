n, h = input().split()
heights = input().split()

n = int(n)
h = int(h)

for i in range(n):
    heights[i] = int(heights[i])

total=0
for i in range(n):
    if heights[i] > h:
        total += 2
    else:
        total += 1
print(total)
