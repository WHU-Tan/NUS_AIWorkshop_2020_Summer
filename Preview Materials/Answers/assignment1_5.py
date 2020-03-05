try:
    ssn = []
    while True:
        sn = input().strip()
        # sn = sys.stdin.readline().strip()
        #若是多输入，strip()默认是以空格分隔，返回一个包含多个字符串的list。
        if sn=='':
            break
        sn = list(sn.split(" "))
        ssn.append(sn)
except:
    pass

k=int(ssn[0][0])
for i in range(0,k):
    price=[]
    line1=ssn[2*i+1]
    line2=ssn[2*i+2]
    n=int(line1[0])
    m=int(line1[1])
    for j in range(0,m):
        price.append(int(line2[j]))
    price.sort()
    Min=10000
    n=n-1

    for j in range(0,m-n):
        s=price[n+j]-price[j]
        if(s<Min):
            Min=s
    print(Min)