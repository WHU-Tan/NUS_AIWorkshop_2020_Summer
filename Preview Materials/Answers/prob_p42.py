line=input()
line=line.split(" ")
a=int(line[0])
b=int(line[1])

while(a!=b):
    if(a>b):
        a=int(a*0.5)
    if(a<b):
        b=int(b*0.5)

print(a)