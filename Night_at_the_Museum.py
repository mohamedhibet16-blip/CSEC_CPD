name = input().strip()
current = 'a'
rotations = 0
for ch in name:
    diff = abs(ord(ch) - ord(current))
    rotations += min(diff, 26 - diff)
    current = ch
print(rotations)
