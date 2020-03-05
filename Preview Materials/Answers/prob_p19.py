para1=input()
para2=input()
para3=input()
x=int(input())
y=int(input())

para1=para1.split(" ")
para2=para2.split(" ")
para3=para3.split(" ")

list_new=[para1,para2,para3]
print(list_new[x-1][y-1])