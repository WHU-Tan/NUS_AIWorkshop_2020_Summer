n=int(input())
a=[0]*101

a.insert(1,1)
for i in range(2,101):
    if(i%2==0):
        a.insert(i,a[int(i*0.5)])
    if(i%2==1):
        a.insert(i,a[i-1]+1)

print(a[n])