line=1
lines=[]
while line !='0':
    line=input()
    lines.append(line.split(' '))

def hardest(n,diff):
    print(max(diff))

for i in range(0,len(lines)-1):
    diffs=[]
    n=int(lines[i][0])
    for j in range(1,n+1):
        diffs.append(int(lines[i][j]))
    hardest(n,diffs)