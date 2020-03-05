n=int(input())
line2=input()
line2=line2.split(" ")

a=int(line2[0])
b=int(line2[1])
c=int(line2[2])

def fibs(num):
#用于保存生成的实例序列
    result = [a,b,c]
#用于生成0到num-2-1的数字
    for i in range(3,n):
#循环数值加入到result列表
        result.append(c*result[i-3]+b*result[i-2]+a*result[i-1])
    return result

result=fibs(n)
print(result[n-1])