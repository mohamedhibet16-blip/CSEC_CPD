n=int(input())
no_of_problem=0
for i in range(n):
    line=input().split()
    for j in range(3):
        line[j]=int(line[j])
    if line.count(1) > line.count(0):
        no_of_problem += 1
    else:
        no_of_problem += 0
print(no_of_problem)
