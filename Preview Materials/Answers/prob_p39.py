n=int(input())
new=[]
summary=0

def isPrime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False

def isSquare(num):    
    a = int(num**0.5)
    return a * a == num

for i in range(1,n+1):
    if(i==1):
        new.insert(i-1,10)
    elif (i>1 and isPrime(i)==True):
        new.insert(i-1,i**2)
    elif (i>1 and isSquare(i)==True):
        new.insert(i-1,2*(i**0.5)+1)
    else:
        new.insert(i-1,int(i**0.5))

for i in range(0,n):
    summary+=new[i]

print(int(summary))