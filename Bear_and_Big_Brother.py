a,b = input().split()
a=int(a)
b=int(b)
year=0
for i in range(10):
    a = 3*a 
    b = 2*b
    year += 1
    if a > b:
        print(year)
        break
