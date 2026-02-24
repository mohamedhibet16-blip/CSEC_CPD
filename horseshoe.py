col=list(map(int,input().split()))
shoe=0
col.sort()
for i in range(1,len(col)):
    if col[i]==col[i-1]:
        shoe+=1
print(shoe)
