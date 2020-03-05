n=int(input())
summary=0
a=[]
out=[]

line2=input()
line2=line2.split(" ")

for i in range(0,n):
    a.append(int(line2[i]))

for i in range(0,n):
    for j in range(1,a[i]+1):
        summary+=(j*j)
    out.append(summary)
    summary=0

print(" ".join(str(i) for i in out))