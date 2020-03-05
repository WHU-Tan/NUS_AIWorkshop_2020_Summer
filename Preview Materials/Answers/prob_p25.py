sen=[]
state_new=[]

for i in range(0,3):
    sen.append(input())
state=input()
state_num=state.split(" ")
for i in range(0,3):
    state_new.append(int(state_num[i]))

if(state_new[0]==1):
    #first turn
    temp=sen[1]
    sen[1]=sen[0]
    sen[0]=temp
if(state_new[1]==1):
    temp=sen[1]
    sen[1]=sen[2]
    sen[2]=temp

if(state_new[2]==1):
    temp=sen[0]
    sen[0]=sen[2]
    sen[2]=temp

for i in range(0,3):
    print(sen[i])