from queue import Queue
line1=input()
line1=line1.split(" ")
n=int(line1[0])
k=int(line1[1])
boy=[]
girl=[]
cake=[]
cnt=0

line2=input()
line2=line2.split(" ")
for i in range(0,n):
    girl.append(int(line2[2*i]))
    boy.append(int(line2[2*n-2*i-1]))

line3=input()
line3=line3.split(" ")
for i in range(0,k):
    cake.append(int(line3[i]))

while(len(cake)!=0):
    for i in range(0,k):
        break_flag=False
        while(cnt==0 and break_flag==False):
            for j in range(0,n):
                if(cake[0]<=girl[j]):
                    print(2*j+1)
                    cnt=1
                    break_flag=True
                    del cake[0]
                    break

        while(cnt==1 and break_flag==False):
            for j in range(0,n):
                if(cake[0]<=boy[j]):
                    print(2*n-2*j)
                    cnt=0
                    break_flag=True
                    del cake[0]
                    break