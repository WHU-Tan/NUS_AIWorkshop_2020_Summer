N=[]
M=[]

t=int(input())
for i in range(0,t):
    line=input()
    line=line.split(" ")
    N.append(int(line[0]))
    M.append(int(line[1]))

def MONKEY(n,k):
    index=0
    people=list(range(1,n+1))
    while True:
        if len(people)==1:
            print(people[0])
            break
        index=(index+(k-1))%len(people)
        #print('kill:',people[index])
        del people[index]

for i in range(0,t):
    MONKEY(N[i],M[i])