cal=list(map(int,input().split()))
x=input()
tot_cal=0
for i in x:
    tot_cal += cal[int(i)-1]
print(tot_cal)
