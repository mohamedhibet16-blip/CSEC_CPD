n=int(input())
s=input()
s.upper()
if s.count('A') > s.count('D'):
    print("Anton")
elif s.count('A') < s.count('D'):
    print("Danik")
else:
    print("Friendship")
