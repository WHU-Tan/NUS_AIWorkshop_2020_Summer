num=input()
num_new=num.split()
a=[]
for i in range(0,5):
    a.append(int(num_new[i]))

if(not(((a[0]&a[1])<=a[4])and((a[2]+a[3])>a[4]))):
    print("False")
else:
    if(((a[2]|a[3])<a[0])and((a[3]*a[4])>=a[4])):
        print("False")
    else:
        print("True")