line1=int(input())
line2=int(input())
line3=int(input())


def isPerfectSquare(num):
    left = num%10
    if(not(left==0 or left==1 or left==4 or left==5 or left==6 or left==9)):
        print('False')
    else:
        for i in range(1,20,2):
                num = num - i
                if(num<=0):
                    break
        if(num==0):
            print('True')
        else:
            print('False')

isPerfectSquare(line1)
isPerfectSquare(line2)
isPerfectSquare(line3)