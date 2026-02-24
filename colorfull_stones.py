s = input().strip()
t = input().strip()

pos = 0  # 0-based index

for c in t:
    if s[pos] == c:
        pos += 1

print(pos + 1)  # convert to 1-based index
