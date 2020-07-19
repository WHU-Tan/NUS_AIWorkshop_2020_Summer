def count(n):   
    A = [0] * (n + 1) 
    B = [0] * (n + 1) 
    A[0] = 1
    A[1] = 0
    B[0] = 0
    B[1] = 1
    for i in range(2, n+1): 
        A[i] = A[i - 2] + 2 * B[i - 1] 
        B[i] = A[i - 1] + B[i - 2]       
    return A[n] 
  
line=1
lines=[]
while line !='-1':
    line=input()
    lines.append(int(line))
for i in range(0, len(lines)-1):
    if(lines[i]!=0):
        print(count(lines[i]))
    if(lines[i]==0):
        print(1)