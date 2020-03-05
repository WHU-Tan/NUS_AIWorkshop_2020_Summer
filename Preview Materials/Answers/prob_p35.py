line1=input()
line1=line1.split(" ")
n=int(line1[0])
k=int(line1[1])
cnt=0


for i in range(1,n):
    if cnt<k:
        is_mul_3=i%3
        is_mul_5=i%5
        oneth=i%10
        tenth=(i-i%10)/10
        if(is_mul_3!=0 and is_mul_5!=0 and (oneth!=3 and oneth!=5) and (tenth!=3 and tenth!=5)):
            print(i)
            cnt+=1
    else:
        break