out=[]
while(1):
    temp=input()
    n=int(temp)
    if(n==0):
        break
    else:
        if (n>=3):
            out.append("Bob")
        else:
            out.append("Alice")

for i in range(0,len(out)):
    print(out[i])