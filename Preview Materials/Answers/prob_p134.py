line = []

def reverse(str):
    return str[::-1]

def Decoder(n,sentence):
    slide=[]
    a=[]
    num=int(len(sentence)/n)
    for i in range(0,num):
        slide.append(sentence[n*i:n*(i+1)])
        if(i%2!=0):
            slide[i]=reverse(slide[i])
    for i in range(0,n):
        for j in range(0,num):
            a.append(slide[j][i])
    print(''.join(a))

while True:
    inputs=input()
    if(inputs!='0'):
        line.append(inputs)
    else:
        break

for k in range(0,len(line),2):
    Decoder(int(line[k]),line[k+1])