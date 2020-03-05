a=[]

line1=input()
line1=line1.split(" ")
n=int(line1[0])
k=int(line1[1])

line2=input()
line2=line2.split(" ")

for i in range(0,n):
    a.append(int(line2[i]))

print(a.count(k))