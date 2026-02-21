n=int(input())
event=list(map(int,input().split()))
start=0
crime=0
police=0
for i in event:
    if i == -1:
        if police > 0:
            police -= 1
        else:
            crime += 1
    else:
        police += i 
print(crime)
