n=int(input())
cnt=0

for j in range(2,n+1):
    for i in range(2,j):
        if(j%i)==0:
            break
    else:
        cnt+=1
print(cnt)        