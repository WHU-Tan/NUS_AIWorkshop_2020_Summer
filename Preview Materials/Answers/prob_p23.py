num=input()
num_new=num.split(" ")
a=int(num_new[0])
n=int(num_new[1])

if(((a>>n))&1):
    print('True')
else:
    print('False')