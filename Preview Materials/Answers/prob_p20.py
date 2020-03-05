items=[]
num=[]
for i in range(0,10):
    key=input()
    value=i
    keyValue=[key,value]
    items.append(keyValue)
d=dict(items)

for i in range(0,3):
    num.append(d[input()])
print(num[0]*100+num[1]*10+num[2])