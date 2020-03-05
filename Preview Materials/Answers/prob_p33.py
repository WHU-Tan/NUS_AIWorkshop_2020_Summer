N=int(input())
cnt=0
summary=0

for j in range(2,1000):
    for i in range(2,j):
        if(j%i)==0:
            break
    else:
        cnt+=1
        summary+=j
    if(summary>=N):
        break		

print(cnt)