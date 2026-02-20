n=int(input())
s=input()
stone=0
for i in range(1,n):
    if s[i]==s[i-1]:
        stone+=1
print(stone)
