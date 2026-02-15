n=int(input())
box=input().split()
for i in range(n):
    box[i]=int(box[i])
box.sort()
for i in box:
    print(i," ", end="")
