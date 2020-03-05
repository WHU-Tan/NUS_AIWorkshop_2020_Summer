string=[]
leng=[]
flag=[0,0,0]
exit_flag=0

for i in range(0,3):
    string.append(input())
    leng.append(len(string[i]))
mystring=input()
length=leng[0]+leng[1]+leng[2]
""" for i in range(0,3):
    for j in range(0,len(mystring),leng[i]):
        if(string[i]==mystring[j:j+1]):
            flag[i]=1
            exit_flag=1
            break
    if(not exit_flag):
        break """

if(mystring[0:leng[0]]==string[0] and mystring[leng[0]:(leng[0]+leng[1])]==string[1] and mystring[(leng[0]+leng[1]):length]==string[2]):
    print('No')
else:
    if(mystring[0:leng[0]]==string[0] and mystring[leng[0]:(leng[0]+leng[2])]==string[2] and mystring[(leng[0]+leng[2]):length]==string[1]):
        print('No')
    else:
        if(mystring[0:leng[1]]==string[1] and mystring[leng[1]:(leng[1]+leng[2])]==string[2] and mystring[(leng[1]+leng[2]):length]==string[0]):
            print('No')
        else:
            if(mystring[0:leng[1]]==string[1] and mystring[leng[1]:(leng[1]+leng[0])]==string[0] and mystring[(leng[1]+leng[0]):length]==string[2]):
                print('No')
            else:
                if(mystring[0:leng[2]]==string[2] and mystring[leng[2]:(leng[2]+leng[0])]==string[0] and mystring[(leng[2]+leng[0]):length]==string[1]):
                    print('No')
                else:
                    if(mystring[0:leng[2]]==string[2] and mystring[leng[2]:(leng[2]+leng[1])]==string[1] and mystring[(leng[2]+leng[1]):length]==string[0]):
                        print('No')
                    else:
                        print('Yes')
                
