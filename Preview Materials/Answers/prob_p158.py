col=int(input())
outputs=[]
while(col!=0):
    string=input()
    row=int((len(string))/col)
    b=""
    for i in range(0,row):
        if i%2==0:
            b+=string[i*col:(i+1)*col]
        else:
            b+=(string[i*col:(i+1)*col])[::-1]
    c=""
    for k in range(0,col):
        for p in range(0,row):
            c+=b[k+p*col]
    outputs.append(c)
    col=int(input())

for i in range(0,len(outputs)):
    print(outputs[i])