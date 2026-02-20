n=int(input())
num=list(map(int,input().split()))
turn="sereja"
start=0
last=n-1
Sereja=0
Dema=0
for i in range(n):
    if num[start] > num[last]:
        max=num[start]
        start += 1
    else:
        max=num[last]
        last -= 1
    if turn=="sereja":
        Sereja += max
        turn="dema"
    else:
        Dema += max
        turn="sereja"
print(Sereja,Dema)
