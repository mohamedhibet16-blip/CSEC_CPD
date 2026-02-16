no_of_magnet=int(input())
first=input()
group=1
for i in range(no_of_magnet - 1):
    next=input()
    if first != next:
        group+=1
    first = next
print(group)    
