for i in range(5):
    lines= input().split()
    for j in range(5):
        lines[j]=int(lines[j])
        if lines[j]==1:
            x,y=i,j  
a=abs(x-2)
b=abs(y-2)
print(a+b)
